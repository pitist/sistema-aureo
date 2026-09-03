#!/usr/bin/env python3
import sys, json, re
from pathlib import Path
from collections import defaultdict

RULES = {
    'R01': (r'profundidad', 'Profundidad > 3', 'error'),
    'R02': (r'\d+px', 'Uso de px', 'error'),
    'R03': (r'RelativeLayout', 'Preferir ConstraintLayout', 'warning'),
    'R04': (r'(padding|margin)(Left|Right)', 'Usar Start/End para RTL', 'warning'),
    'R05': (r'ListView|GridView', 'Usar RecyclerView', 'error'),
    'R06': (r'LinearLayout.*layout_weight', 'Weight anidado', 'error'),
    'R07': (r'lineas>80', 'Archivo >80 líneas', 'error'),
    'R08': (r'ID duplicado', 'IDs duplicados', 'error'),
    'R10': (r'ViewGroup vacío anidado', 'ViewGroup vacío', 'warning'),
    'A01': (r'(Activity|Fragment|Composable).*(Retrofit|Room|SQLite|okhttp)', 'Lógica de negocio en UI', 'error'),
    'A04': (r'Activity.*var\s+\w+[:=]', 'Estado en Activity', 'error'),
    'A05': (r'Retrofit\.create\(|Room\.databaseBuilder\(', 'Llamada directa a fuente de datos', 'error'),
    'A06': (r'(?<!@Inject)\s+new\s+\w+\(', 'Instanciación manual', 'error'),
    'A09': (r'class\s+\w+ViewModel[^}]*fun\s+\w+\(', 'ViewModel sin tests', 'error'),
    'A10': (r'runBlocking|Thread\.sleep|\.await\(\)', 'Bloqueo en hilo principal', 'error'),
    'S01': (r'(static\s+Context|addListener[^;]*;(?!.*removeListener)|handler\.postDelayed)', 'Memory leak', 'error'),
    'S02': (r'(Class\.forName\(|DexClassLoader\(|Runtime\.exec\(|ProcessBuilder\(|loadLibrary\([^)]*(?!.*validated))', 'Riesgo de secuestro', 'error'),
    'S127': (r'(SQLiteDatabase\.execSQL\([^)]*\+|Runtime\.exec\([^)]*\+|@Query\([^)]*\+)', 'Inyección (SQL/comandos)', 'error'),
    'P01': (r'Application\.onCreate\(\)\s*\{[^}]*\b(?!.*async)', 'Cold start lento', 'error'),
    'P02': (r'.*\.png$', 'Usar WebP', 'warning'),
    'P03': (r'(LinearLayout|FrameLayout).*background.*', 'Overdraw', 'warning'),
    'P06': (r'<ImageView[^>]*?(?!/>)(?!.*contentDescription)', 'Falta contentDescription', 'warning'),
    'P07': (r'<Button.*android:layout_height="[0-9]+dp"', 'Tamaño de toque <48dp', 'warning'),
    'P08': (r'android:text="[^@"]+"', 'Texto hardcodeado', 'error'),
    'P09': (r'com\.android\.support', 'Dependencia obsoleta', 'warning'),
    'P10': (r'catch\s*\(\s*\w+\s*:\s*Exception\s*\)\s*\{\s*\}', 'Catch vacío', 'error'),
    'C01': (r'\bremember\s*\{[^}]*State\b(?!.*rememberSaveable)', 'Usar rememberSaveable', 'error'),
    'C02': (r'derivedStateOf|State\b.*\blambda\b', 'Recomposición excesiva', 'warning'),
    'C03': (r'class\s+\w+\s*\([^)]*\)\s*\{.*var\s+\w+.*\}', 'Falta @Stable/@Immutable', 'warning'),
    'C04': (r'LaunchedEffect\s*\(\s*Unit\s*\)\s*\{[^}]*\}', 'LaunchedEffect sin cleanup', 'error'),
    'C05': (r'viewModelScope\.launch\s*\{[^}]*\}', 'Usar rememberCoroutineScope', 'warning'),
    'K01': (r'(androidMain|iosMain).*(implementation|api).*', 'Dependencia en plataforma específica', 'error'),
    'K02': (r'\bexpect\b[^;]*;(?!.*\bactual\b)', 'Falta actual para expect', 'error'),
    'K03': (r'\bGson\b|\bJackson\b', 'Usar kotlinx.serialization', 'warning'),
    'P11': (r'versionCode\s+[0-9]+', 'versionCode no semántico', 'warning'),
    'P12': (r'android:icon\s*=\s*"@mipmap/ic_launcher"', 'Icono y label definidos', 'warning'),
    'P13': (r'debug\s*keystore', 'Firma debug en release', 'error'),
    'D01': (r'.github/workflows/.*\.yml', 'CI sin auditoría', 'error'),
    'D02': (r'CHANGELOG\.md', 'Falta CHANGELOG', 'warning'),
    'D03': (r'("password"|"api_key"|"secret")\s*=\s*"[^$]+"', 'Secretos hardcodeados', 'error'),
}

class Auditor:
    def __init__(self, root):
        self.root = Path(root)
        self.reports = []
    def run(self):
        for ext in ['*.xml','*.kt','*.java','*.gradle','*.yml','*.yaml','*.md']:
            for f in self.root.rglob(ext):
                try:
                    content = f.read_text(errors='ignore')
                    for rid, (pat, msg, sev) in RULES.items():
                        if re.search(pat, content, re.DOTALL|re.IGNORECASE):
                            self.reports.append({'file':str(f), 'rule':rid, 'severity':sev, 'msg':msg})
                except: pass
        return self._summary()
    def _summary(self):
        errors = sum(1 for r in self.reports if r['severity']=='error')
        warnings = len(self.reports)-errors
        debt = errors*0.5 + warnings*0.2
        score = max(0, 100 - errors*5 - debt*0.5)
        return {'meta':{'total':len(self.reports),'errors':errors,'warnings':warnings,'debt':round(debt,1),'score':round(score,1),'savings':round(debt*50,2)}, 'files':self.reports[:50]}

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Uso: python3 auditor_completo.py /ruta/al/proyecto")
        sys.exit(1)
    data = Auditor(sys.argv[1]).run()
    with open('reporte_final.json','w') as f: json.dump(data,f,indent=2)
    print(f"\n📊 Score: {data['meta']['score']}% | Deuda: {data['meta']['debt']}h | Ahorro: ${data['meta']['savings']}")
