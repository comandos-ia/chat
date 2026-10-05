import os
import subprocess
from PIL import Image

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT_JPG = os.path.abspath("imagens/og-preview.jpg")
TEMP_HTML = os.path.abspath("temp_og.html")
TEMP_PNG = os.path.abspath("temp_og.png")

HTML_BANNER = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<style>
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; }
body {
    width: 1200px;
    height: 630px;
    overflow: hidden;
    background: #070c18;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(49, 91, 232, 0.25) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(79, 209, 232, 0.2) 0%, transparent 50%),
        radial-gradient(circle at 50% 50%, rgba(116, 84, 214, 0.15) 0%, transparent 60%);
    color: #f1f5f9;
    padding: 38px 46px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    -webkit-font-smoothing: antialiased;
}

/* Header do Banner */
.banner-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}
.brand-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(79, 209, 232, 0.12);
    border: 1px solid rgba(79, 209, 232, 0.35);
    color: #4fd1e8;
    padding: 6px 14px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.14em;
}
.pill-count {
    background: linear-gradient(135deg, #315be8, #7454d6);
    color: white;
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.05em;
    box-shadow: 0 4px 16px rgba(49, 91, 232, 0.4);
}

.hero-title {
    margin-top: 14px;
    max-width: 900px;
}
.hero-title h1 {
    font-size: 38px;
    font-weight: 850;
    line-height: 1.15;
    letter-spacing: -0.03em;
    color: #ffffff;
}
.hero-title h1 span {
    background: linear-gradient(90deg, #4fd1e8, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-title p {
    font-size: 17px;
    color: #cbd5e1;
    margin-top: 8px;
    line-height: 1.4;
    font-weight: 400;
}

/* Grid com Amostra dos Comandos Reais */
.cards-showcase {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 20px;
}
.sample-card {
    background: rgba(15, 23, 42, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 14px;
    padding: 16px 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.45);
    backdrop-filter: blur(8px);
}
.cmd-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.cmd-name {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: 13.5px;
    font-weight: 800;
    color: #60a5fa;
    background: rgba(49, 91, 232, 0.18);
    padding: 3px 8px;
    border-radius: 6px;
    border: 1px solid rgba(49, 91, 232, 0.35);
}
.copy-badge {
    background: #315be8;
    color: white;
    font-size: 10px;
    font-weight: 700;
    padding: 4px 8px;
    border-radius: 6px;
}
.card-title {
    font-size: 15px;
    font-weight: 700;
    color: #f8fafc;
}
.card-desc {
    font-size: 12px;
    color: #94a3b8;
    line-height: 1.4;
}
.mini-preview {
    background: #091024;
    border: 1px solid #1a253d;
    border-radius: 8px;
    padding: 8px 10px;
    font-size: 11px;
    color: #38bdf8;
    display: flex;
    align-items: center;
    gap: 6px;
    font-weight: 600;
}

/* Rodapé do Banner */
.banner-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 14px;
    font-size: 12.5px;
    color: #94a3b8;
}
.features-list {
    display: flex;
    gap: 20px;
}
.feat-item {
    display: flex;
    align-items: center;
    gap: 6px;
    color: #e2e8f0;
    font-weight: 600;
}
.feat-icon {
    color: #4fd1e8;
    font-size: 14px;
}
.site-url {
    color: #60a5fa;
    font-weight: 700;
    letter-spacing: 0.04em;
}
</style>
</head>
<body>

  <div class="banner-head">
    <div class="brand-badge">⚡ BIBLIOTECA PRÁTICA · GESTÃO E LIDERANÇA</div>
    <div class="pill-count">52 COMANDOS PRONTOS</div>
  </div>

  <div class="hero-title">
    <h1>Comandos de IA para <span>pensar, decidir e executar melhor</span>.</h1>
    <p>Catálogo executivo de prompts e atalhos com finalidades, exemplos práticos de uso e ilustrações visuais de resultados para líderes e gestores.</p>
  </div>

  <div class="cards-showcase">
    <!-- Card 1 -->
    <div class="sample-card">
      <div class="cmd-bar">
        <span class="cmd-name">/decisionbrief</span>
        <span class="copy-badge">COPIAR</span>
      </div>
      <div class="card-title">Briefing de Decisão</div>
      <div class="card-desc">Apresenta problema, critérios, riscos e alternativas para decisão executiva.</div>
      <div class="mini-preview">📊 Ilustração do resultado incluída</div>
    </div>

    <!-- Card 2 -->
    <div class="sample-card">
      <div class="cmd-bar">
        <span class="cmd-name">/rootcause</span>
        <span class="copy-badge">COPIAR</span>
      </div>
      <div class="card-title">Análise de Causa-Raiz</div>
      <div class="card-desc">Investiga causas prováveis separando evidências de hipóteses operacionais.</div>
      <div class="mini-preview">🔍 Diagrama visual de causa e efeito</div>
    </div>

    <!-- Card 3 -->
    <div class="sample-card">
      <div class="cmd-bar">
        <span class="cmd-name">/strategicplan</span>
        <span class="copy-badge">COPIAR</span>
      </div>
      <div class="card-title">Plano Estratégico</div>
      <div class="card-desc">Conecta metas a iniciativas, prazos e indicadores de sucesso.</div>
      <div class="mini-preview">🎯 Roadmap e metas visuais</div>
    </div>
  </div>

  <div class="banner-footer">
    <div class="features-list">
      <div class="feat-item"><span class="feat-icon">✓</span> 52 Prompts Testados</div>
      <div class="feat-item"><span class="feat-icon">✓</span> Imagens em Alta Resolução</div>
      <div class="feat-item"><span class="feat-icon">✓</span> Visualização em Lightbox</div>
      <div class="feat-item"><span class="feat-icon">✓</span> Filtros por Categoria</div>
    </div>
    <div class="site-url">comandos-ia.github.io/chat</div>
  </div>

</body>
</html>
"""

def generate():
    with open(TEMP_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_BANNER)

    file_url = "file:///" + TEMP_HTML.replace("\\", "/")
    cmd = [
        EDGE_PATH,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1200,630",
        f"--screenshot={TEMP_PNG}",
        file_url
    ]
    subprocess.run(cmd, check=True)
    
    if os.path.exists(TEMP_PNG):
        img = Image.open(TEMP_PNG).convert("RGB")
        img = img.resize((1200, 630), Image.Resampling.LANCZOS)
        # WhatsApp recomenda imagem < 300KB
        img.save(OUT_JPG, "JPEG", quality=90, optimize=True)
        os.remove(TEMP_PNG)
        print("Novo og-preview.jpg gerado com sucesso!")
        print("Tamanho do arquivo:", os.path.getsize(OUT_JPG), "bytes")

    if os.path.exists(TEMP_HTML):
        os.remove(TEMP_HTML)

if __name__ == "__main__":
    generate()
