import os
import subprocess
import time

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
OUT_DIR = "imagens"

BASE_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif; }
body {
    background: #070c18;
    color: #f1f5f9;
    width: 1376px;
    height: 768px;
    overflow: hidden;
    display: flex;
    -webkit-font-smoothing: antialiased;
}
aside {
    width: 240px;
    background: #091024;
    border-right: 1px solid #1a253d;
    padding: 24px 18px;
    display: flex;
    flex-direction: column;
    gap: 22px;
}
.brand {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #38bdf8;
}
.brand-icon {
    width: 28px;
    height: 28px;
    background: linear-gradient(135deg, #0284c7, #38bdf8);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 15px;
    font-weight: 900;
}
.nav-group {
    display: flex;
    flex-direction: column;
    gap: 6px;
}
.nav-title {
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: #475569;
    padding: 0 8px;
    margin-bottom: 2px;
}
.nav-link {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 12px;
    border-radius: 8px;
    font-size: 12.5px;
    color: #94a3b8;
    font-weight: 500;
}
.nav-link.active {
    background: #132247;
    color: #38bdf8;
    border: 1px solid #1e3a8a;
    font-weight: 600;
}
main {
    flex: 1;
    padding: 24px 28px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    background: radial-gradient(circle at 85% 15%, #151d3b 0%, #070c18 65%);
}
.top-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px solid #1a253d;
    padding-bottom: 14px;
}
.top-title h1 {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: -0.02em;
    color: #f8fafc;
}
.top-title p {
    font-size: 12px;
    color: #64748b;
    margin-top: 3px;
}
.badge-pill {
    padding: 5px 13px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.badge-blue { background: rgba(56,189,248,0.12); color: #38bdf8; border: 1px solid rgba(56,189,248,0.3); }
.badge-emerald { background: rgba(52,211,153,0.12); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
.badge-amber { background: rgba(251,191,36,0.12); color: #fbbf24; border: 1px solid rgba(251,191,36,0.3); }
.badge-purple { background: rgba(192,132,252,0.12); color: #c084fc; border: 1px solid rgba(192,132,252,0.3); }
.badge-rose { background: rgba(251,113,133,0.12); color: #fb7185; border: 1px solid rgba(251,113,133,0.3); }

.card {
    background: #0b1329;
    border: 1px solid #1a253d;
    border-radius: 12px;
    padding: 16px 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}
.card-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 12px;
}
.card-head h2 {
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #94a3b8;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 6px;
}
"""

TEMPLATES = {
    # 1. 1:1
    "reuniao_1on1.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid {{ display: grid; grid-template-columns: 1.6fr 1fr; gap: 16px; flex: 1; }}
    .topic {{ background: #101c38; border-radius: 10px; padding: 13px 15px; margin-bottom: 10px; border-left: 4px solid #38bdf8; }}
    .topic.amber {{ border-left-color: #fbbf24; }}
    .topic.purple {{ border-left-color: #c084fc; }}
    .topic.emerald {{ border-left-color: #34d399; }}
    .topic h3 {{ font-size: 13px; font-weight: 600; color: #e2e8f0; margin-bottom: 4px; }}
    .topic p {{ font-size: 12px; color: #94a3b8; line-height: 1.4; }}
    .kpi-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 14px; }}
    .kpi {{ background: #101c38; border-radius: 10px; padding: 12px; text-align: center; border: 1px solid #1a253d; }}
    .kpi strong {{ display: block; font-size: 22px; color: #f8fafc; font-weight: 800; }}
    .kpi span {{ font-size: 11px; color: #64748b; text-transform: uppercase; font-weight: 600; }}
    .task {{ display: flex; align-items: center; justify-content: space-between; padding: 10px 12px; background: #101c38; border-radius: 8px; font-size: 12px; margin-bottom: 8px; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">1:1</div> Gestão de Pessoas</div>
      <div class="nav-group"><div class="nav-title">Navegação</div><div class="nav-link active">🤝 Reunião 1:1</div><div class="nav-link">🎯 Metas & OKRs</div><div class="nav-link">📈 Carreira</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Alinhamento Individual (1:1) · Pauta e Acompanhamento</h1><p>Encontro quinzenal entre líder e liderado · Foco em autonomia, desbloqueios e escuta ativa</p></div>
        <span class="badge-pill badge-blue">Status: Concluído</span>
      </div>
      <div class="grid">
        <div class="card">
          <div class="card-head"><h2>📋 Blocos Estruturados da Pauta</h2><span class="badge-pill badge-purple">45 Minutos</span></div>
          <div class="topic"><h3>1. Check-in Pessoal & Nível de Energia</h3><p>Como foram as duas últimas semanas? Houve sobrecarga ou equilíbrio saudável?</p></div>
          <div class="topic amber"><h3>2. Desafios & Obstáculos Atuais</h3><p>Gargalo na validação de escopo com o time de engenharia atrasando entrega de sprint.</p></div>
          <div class="topic purple"><h3>3. Desenvolvimento e Próximos Passos</h3><p>Oportunidade de liderar a apresentação de resultados para a diretoria na próxima terça.</p></div>
          <div class="topic emerald"><h3>4. Feedback Bidirecional</h3><p>Troca rápida sobre clareza das prioridades e suporte oferecido pela liderança.</p></div>
        </div>
        <div style="display:flex; flex-direction:column; gap:16px;">
          <div class="card">
            <div class="card-head"><h2>📊 Indicadores de Acompanhamento</h2></div>
            <div class="kpi-row">
              <div class="kpi"><strong>94%</strong><span>Compromissos Entregues</span></div>
              <div class="kpi"><strong>4.9★</strong><span>Índice de Confiança</span></div>
            </div>
          </div>
          <div class="card" style="flex:1;">
            <div class="card-head"><h2>✅ Acordos Firmados</h2></div>
            <div class="task"><span>Revisar documentação técnica até quinta</span><span class="badge-pill badge-emerald">Liderado</span></div>
            <div class="task"><span>Agendar conversa com Gerente de Produto</span><span class="badge-pill badge-blue">Gestor</span></div>
            <div class="task"><span>Mapear 2 cursos de liderança desejados</span><span class="badge-pill badge-purple">Liderado</span></div>
          </div>
        </div>
      </div>
    </main></body></html>""",

    # 2. Avaliação de Desempenho
    "avaliacao_desempenho.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; flex: 1; }}
    .bar-group {{ margin-bottom: 12px; }}
    .bar-label {{ display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 5px; font-weight: 600; color: #cbd5e1; }}
    .bar-track {{ height: 10px; background: #162446; border-radius: 999px; overflow: hidden; }}
    .bar-fill {{ height: 100%; border-radius: 999px; }}
    .ninebox {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; margin-top: 10px; }}
    .box-cell {{ background: #101c38; border: 1px solid #1a253d; border-radius: 8px; padding: 10px; text-align: center; font-size: 11px; }}
    .box-cell.highlight {{ background: rgba(56,189,248,0.2); border-color: #38bdf8; font-weight: 700; color: #38bdf8; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">★</div> Avaliação</div>
      <div class="nav-group"><div class="nav-title">Ciclo</div><div class="nav-link active">📊 Desempenho</div><div class="nav-link">🎯 Metas</div><div class="nav-link">🏆 Mérito</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Matriz de Avaliação de Desempenho e Competências</h1><p>Consolidação de entregas operacionais, comportamentos de liderança e impacto no negócio</p></div>
        <span class="badge-pill badge-emerald">Ciclo Anual 2025</span>
      </div>
      <div class="grid">
        <div class="card">
          <div class="card-head"><h2>🎯 Competências Chave & Avaliação de Entrega</h2><span class="badge-pill badge-blue">Score Geral: 4.6 / 5.0</span></div>
          <div class="bar-group">
            <div class="bar-label"><span>Execução e Foco em Resultados</span><span>95% (Superou)</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:95%; background:#38bdf8;"></div></div>
          </div>
          <div class="bar-group">
            <div class="bar-label"><span>Capacidade Analítica e Resolução de Problemas</span><span>90% (Superou)</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:90%; background:#34d399;"></div></div>
          </div>
          <div class="bar-group">
            <div class="bar-label"><span>Comunicação e Trabalho em Equipe</span><span>88% (Atingiu)</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:88%; background:#c084fc;"></div></div>
          </div>
          <div class="bar-group">
            <div class="bar-label"><span>Liderança e Autonomia Decisória</span><span>85% (Atingiu)</span></div>
            <div class="bar-track"><div class="bar-fill" style="width:85%; background:#fbbf24;"></div></div>
          </div>
        </div>
        <div class="card">
          <div class="card-head"><h2>🧭 Posicionamento na Matriz 9-Box</h2><span class="badge-pill badge-purple">Alto Potencial</span></div>
          <p style="font-size:11px; color:#64748b; margin-bottom:8px;">Desempenho x Potencial de Crescimento</p>
          <div class="ninebox">
            <div class="box-cell">Futuro Líder</div>
            <div class="box-cell highlight">⭐ Talento Top</div>
            <div class="box-cell">Estrela</div>
            <div class="box-cell">Especialista</div>
            <div class="box-cell">Forte Desempenho</div>
            <div class="box-cell">Alto Impacto</div>
            <div class="box-cell">Risco</div>
            <div class="box-cell">Eficaz</div>
            <div class="box-cell">Consistente</div>
          </div>
        </div>
      </div>
    </main></body></html>""",

    # 3. Plano de Sucessão
    "plano_sucessao.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 8px; }}
    .table th {{ text-align: left; padding: 10px 12px; background: #101c38; color: #94a3b8; font-weight: 700; text-transform: uppercase; font-size: 10.5px; border-bottom: 2px solid #1a253d; }}
    .table td {{ padding: 12px; border-bottom: 1px solid #14203b; color: #cbd5e1; }}
    .ready-now {{ color: #34d399; font-weight: 700; }}
    .ready-med {{ color: #fbbf24; font-weight: 700; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">👥</div> Sucessão</div>
      <div class="nav-group"><div class="nav-title">Continuidade</div><div class="nav-link active">🏛️ Cargos Críticos</div><div class="nav-link">⭐ Pipeline</div><div class="nav-link">🛡️ Mitigação</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Mapa Estratégico de Sucessão · Cargos Críticos</h1><p>Mapeamento de funções vitais, risco de perda e prontidão de sucessores internos</p></div>
        <span class="badge-pill badge-amber">Risco de Continuidade: Controlado</span>
      </div>
      <div class="card" style="flex:1;">
        <div class="card-head"><h2>🏢 Pipeline de Sucessores e Prontidão de Assunção</h2><span class="badge-pill badge-blue">4 Cargos Críticos Mapeados</span></div>
        <table class="table">
          <thead>
            <tr><th>Cargo Crítico</th><th>Titular Atual</th><th>Risco de Saída</th><th>Sucessor Primário</th><th>Prontidão</th><th>Plano de Desenvolvimento</th></tr>
          </thead>
          <tbody>
            <tr><td><strong>Gerente de Operações</strong></td><td>Carlos Alberto M.</td><td><span class="badge-pill badge-amber">Médio</span></td><td>Mariana Souza</td><td><span class="ready-now">● Pronta Agora</span></td><td>Alinhamento de orçamento e diretoria</td></tr>
            <tr><td><strong>Coordenador de Torre de Controle</strong></td><td>Fernanda Ramos</td><td><span class="badge-pill badge-rose">Alto</span></td><td>Lucas Ferreira</td><td><span class="ready-med">● 6 a 12 meses</span></td><td>Gestão de crises e negociação</td></tr>
            <tr><td><strong>Especialista de Processos</strong></td><td>Roberto Albuquerque</td><td><span class="badge-pill badge-emerald">Baixo</span></td><td>Juliana Paiva</td><td><span class="ready-now">● Pronta Agora</span></td><td>Liderança de projetos transversais</td></tr>
            <tr><td><strong>Líder Técnico de Integrações</strong></td><td>André Santos</td><td><span class="badge-pill badge-amber">Médio</span></td><td>Pedro Henrique</td><td><span class="ready-med">● 1 a 2 anos</span></td><td>Arquitetura de sistemas em nuvem</td></tr>
          </tbody>
        </table>
      </div>
    </main></body></html>""",

    # 4. Fluxo de Reunião
    "fluxo_reuniao.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .steps {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1; }}
    .step-card {{ background: #0b1329; border: 1px solid #1a253d; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; gap: 14px; position: relative; }}
    .step-num {{ width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 800; }}
    .num-1 {{ background: rgba(56,189,248,0.2); color: #38bdf8; border: 1px solid #38bdf8; }}
    .num-2 {{ background: rgba(251,191,36,0.2); color: #fbbf24; border: 1px solid #fbbf24; }}
    .num-3 {{ background: rgba(52,211,153,0.2); color: #34d399; border: 1px solid #34d399; }}
    .step-card h3 {{ font-size: 14px; font-weight: 700; color: #f8fafc; margin-bottom: 4px; }}
    .step-item {{ background: #101c38; border-radius: 8px; padding: 11px; font-size: 12px; color: #94a3b8; border-left: 3px solid #38bdf8; line-height: 1.4; }}
    .step-item.amber {{ border-left-color: #fbbf24; }}
    .step-item.green {{ border-left-color: #34d399; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">⏱️</div> Reuniões</div>
      <div class="nav-group"><div class="nav-title">Produtividade</div><div class="nav-link active">🔄 Fluxo Padrão</div><div class="nav-link">📝 Pautas</div><div class="nav-link">📌 Ações</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Fluxo de Reunião Eficaz · Do Planejamento à Ação</h1><p>Metodologia de 3 fases para reuniões focadas em decisão e sem desperdício de tempo</p></div>
        <span class="badge-pill badge-blue">Timebox: 45 Minutos Máx</span>
      </div>
      <div class="steps">
        <div class="step-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="step-num num-1">1</div><span class="badge-pill badge-blue">Pré-Reunião</span>
          </div>
          <h3>Preparação & Contexto</h3>
          <div class="step-item">Pauta clara enviada com 24h de antecedência contendo o objetivo exato.</div>
          <div class="step-item">Material prévio compartilhado (leitura assíncrona de no máximo 5 minutos).</div>
          <div class="step-item">Apenas participantes indispensáveis para a tomada de decisão convocados.</div>
        </div>
        <div class="step-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="step-num num-2">2</div><span class="badge-pill badge-amber">Durante</span>
          </div>
          <h3>Condução & Decisão</h3>
          <div class="step-item amber">Início pontual com alinhamento da decisão que precisa ser tomada.</div>
          <div class="step-item amber">Gestão ativa do timebox: 10 min discussão, 20 min debate, 15 min consenso.</div>
          <div class="step-item amber">Estacionamento de ideias para assuntos paralelos que fogem da pauta.</div>
        </div>
        <div class="step-card">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div class="step-num num-3">3</div><span class="badge-pill badge-emerald">Pós-Reunião</span>
          </div>
          <h3>Ação & Accountability</h3>
          <div class="step-item green">Ata síntese disparada em até 2 horas (Decisões + Responsáveis + Prazos).</div>
          <div class="step-item green">Inclusão direta dos planos de ação no sistema de gestão de tarefas.</div>
          <div class="step-item green">Acompanhamento dos prazos no início do ciclo seguinte.</div>
        </div>
      </div>
    </main></body></html>""",

    # 5. Custo de Reunião
    "custo_reuniao.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 16px; flex: 1; }}
    .metric-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 14px; }}
    .metric-box {{ background: #101c38; border: 1px solid #1a253d; border-radius: 10px; padding: 14px; }}
    .metric-box strong {{ display: block; font-size: 24px; color: #f8fafc; font-weight: 800; }}
    .metric-box span {{ font-size: 11px; color: #64748b; text-transform: uppercase; }}
    .row-part {{ display: flex; justify-content: space-between; align-items: center; padding: 9px 12px; background: #101c38; border-radius: 8px; margin-bottom: 8px; font-size: 12px; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">💰</div> Finanças</div>
      <div class="nav-group"><div class="nav-title">ROI de Tempo</div><div class="nav-link active">💵 Custo de Encontro</div><div class="nav-link">⏱️ Eficiência</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Calculadora de Custo de Reunião Corporativa</h1><p>Impacto financeiro e custo de oportunidade das horas alocadas em agendas recorrentes</p></div>
        <span class="badge-pill badge-rose">Impacto Financeiro Direto</span>
      </div>
      <div class="grid">
        <div class="card">
          <div class="card-head"><h2>📊 Resumo Executivo de Investimento</h2><span class="badge-pill badge-amber">Duração: 60 Minutos</span></div>
          <div class="metric-grid">
            <div class="metric-box"><strong style="color:#fb7185;">R$ 2.450,00</strong><span>Custo Deste Encontro</span></div>
            <div class="metric-box"><strong style="color:#fbbf24;">R$ 9.800,00</strong><span>Custo Mensal (4x)</span></div>
            <div class="metric-box"><strong style="color:#38bdf8;">8 Pessoas</strong><span>Participantes Convocados</span></div>
            <div class="metric-box"><strong style="color:#34d399;">R$ 306,25</strong><span>Custo Médio / Hora</span></div>
          </div>
          <div style="background:#101c38; border-radius:10px; padding:12px; font-size:12px; color:#cbd5e1; border-left:4px solid #38bdf8;">
            💡 <strong>Análise de Oportunidade:</strong> Se este alinhamento for reduzido para 30 minutos ou substituído por comunicação assíncrona, a economia anual estimada é de <strong>R$ 58.800,00</strong> em horas de liderança.
          </div>
        </div>
        <div class="card">
          <div class="card-head"><h2>👥 Composição por Nível de Função</h2></div>
          <div class="row-part"><span>1x Diretor de Operações</span><span style="color:#fb7185; font-weight:700;">R$ 800/h</span></div>
          <div class="row-part"><span>2x Gerentes de Área</span><span style="color:#fbbf24; font-weight:700;">R$ 850/h</span></div>
          <div class="row-part"><span>3x Coordenadores</span><span style="color:#38bdf8; font-weight:700;">R$ 540/h</span></div>
          <div class="row-part"><span>2x Especialistas Sênior</span><span style="color:#34d399; font-weight:700;">R$ 260/h</span></div>
        </div>
      </div>
    </main></body></html>""",

    # 6. Mapa de Capacidade
    "mapa_capacidade.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid-team {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; flex: 1; }}
    .team-col {{ background: #0b1329; border: 1px solid #1a253d; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }}
    .team-col h3 {{ font-size: 13px; font-weight: 700; color: #f8fafc; }}
    .rate {{ font-size: 26px; font-weight: 800; }}
    .rate.crit {{ color: #fb7185; }}
    .rate.warn {{ color: #fbbf24; }}
    .rate.good {{ color: #34d399; }}
    .bar {{ height: 8px; background: #162446; border-radius: 999px; overflow: hidden; }}
    .bar-in {{ height: 100%; border-radius: 999px; }}
    .member-mini {{ background: #101c38; border-radius: 6px; padding: 8px; font-size: 11px; display: flex; justify-content: space-between; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">📈</div> Capacidade</div>
      <div class="nav-group"><div class="nav-title">Carga de Trabalho</div><div class="nav-link active">🗺️ Mapa Geral</div><div class="nav-link">⚖️ Balanceamento</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Mapa Visual de Capacidade Operacional da Equipe</h1><p>Horas disponíveis vs. alocadas por frente de trabalho · Prevenção de gargalos e sobrecargas</p></div>
        <span class="badge-pill badge-purple">Mês Corrente</span>
      </div>
      <div class="grid-team">
        <div class="team-col">
          <h3>Torre de Controle</h3>
          <div class="rate crit">112%</div>
          <div class="bar"><div class="bar-in" style="width:100%; background:#fb7185;"></div></div>
          <span class="badge-pill badge-rose" style="text-align:center;">Sobrecarga Crítica</span>
          <div class="member-mini"><span>Ana Clara (Coord)</span><strong>48h/sem</strong></div>
          <div class="member-mini"><span>Rafael Santos</span><strong>45h/sem</strong></div>
        </div>
        <div class="team-col">
          <h3>Gestão de Risco</h3>
          <div class="rate warn">92%</div>
          <div class="bar"><div class="bar-in" style="width:92%; background:#fbbf24;"></div></div>
          <span class="badge-pill badge-amber" style="text-align:center;">Atenção Máxima</span>
          <div class="member-mini"><span>Bruno Lima</span><strong>41h/sem</strong></div>
          <div class="member-mini"><span>Camila Rocha</span><strong>39h/sem</strong></div>
        </div>
        <div class="team-col">
          <h3>Processos & Qualidade</h3>
          <div class="rate good">82%</div>
          <div class="bar"><div class="bar-in" style="width:82%; background:#34d399;"></div></div>
          <span class="badge-pill badge-emerald" style="text-align:center;">Zona Saudável</span>
          <div class="member-mini"><span>Diego Martins</span><strong>36h/sem</strong></div>
          <div class="member-mini"><span>Larissa Duarte</span><strong>34h/sem</strong></div>
        </div>
        <div class="team-col">
          <h3>Atendimento Especial</h3>
          <div class="rate good">75%</div>
          <div class="bar"><div class="bar-in" style="width:75%; background:#38bdf8;"></div></div>
          <span class="badge-pill badge-blue" style="text-align:center;">Capacidade Livre</span>
          <div class="member-mini"><span>Lucas Vieira</span><strong>30h/sem</strong></div>
          <div class="member-mini"><span>Fernanda Vaz</span><strong>32h/sem</strong></div>
        </div>
      </div>
    </main></body></html>""",

    # 7. Matriz de Riscos
    "matriz_riscos.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid-m {{ display: grid; grid-template-columns: 1fr 340px; gap: 16px; flex: 1; }}
    .matrix-box {{ display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: repeat(5, 1fr); gap: 6px; height: 380px; }}
    .m-cell {{ border-radius: 6px; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; color: #fff; position: relative; }}
    .c-green {{ background: #065f46; }}
    .c-yellow {{ background: #854d0e; }}
    .c-orange {{ background: #9a3412; }}
    .c-red {{ background: #991b1b; }}
    .m-point {{ width: 22px; height: 22px; border-radius: 50%; background: #fff; color: #0f172a; display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 900; box-shadow: 0 0 10px rgba(255,255,255,0.8); }}
    .risk-item {{ background: #101c38; border-radius: 8px; padding: 10px 12px; margin-bottom: 8px; font-size: 12px; display: flex; align-items: center; gap: 8px; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">⚠️</div> Riscos</div>
      <div class="nav-group"><div class="nav-title">Governança</div><div class="nav-link active">🎯 Matriz 5x5</div><div class="nav-link">🛡️ Mitigações</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Matriz de Probabilidade e Impacto (5x5)</h1><p>Classificação visual de riscos operacionais, regulatórios e tecnológicos</p></div>
        <span class="badge-pill badge-rose">3 Riscos Críticos</span>
      </div>
      <div class="grid-m">
        <div class="card" style="display:flex; flex-direction:column; justify-content:center;">
          <div class="card-head"><h2>Probabilidade (Vertical) x Impacto (Horizontal)</h2><span class="badge-pill badge-amber">Metodologia Padrão</span></div>
          <div class="matrix-box">
            <div class="m-cell c-yellow"></div><div class="m-cell c-orange"></div><div class="m-cell c-red"><div class="m-point">R1</div></div><div class="m-cell c-red"><div class="m-point">R2</div></div><div class="m-cell c-red"></div>
            <div class="m-cell c-yellow"></div><div class="m-cell c-yellow"></div><div class="m-cell c-orange"></div><div class="m-cell c-red"><div class="m-point">R3</div></div><div class="m-cell c-red"></div>
            <div class="m-cell c-green"></div><div class="m-cell c-yellow"></div><div class="m-cell c-yellow"></div><div class="m-cell c-orange"></div><div class="m-cell c-orange"></div>
            <div class="m-cell c-green"></div><div class="m-cell c-green"></div><div class="m-cell c-yellow"></div><div class="m-cell c-yellow"></div><div class="m-cell c-orange"></div>
            <div class="m-cell c-green"></div><div class="m-cell c-green"></div><div class="m-cell c-green"></div><div class="m-cell c-yellow"></div><div class="m-cell c-yellow"></div>
          </div>
        </div>
        <div class="card">
          <div class="card-head"><h2>🚨 Riscos Prioritários</h2></div>
          <div class="risk-item"><div class="m-point" style="background:#fb7185; color:#fff;">R1</div><div><strong>Falha de Integração API</strong><div style="font-size:11px; color:#64748b;">Impacto Crítico · Resp: Time TI</div></div></div>
          <div class="risk-item"><div class="m-point" style="background:#fb7185; color:#fff;">R2</div><div><strong>Atraso Liberação Alfândega</strong><div style="font-size:11px; color:#64748b;">Impacto Alto · Resp: Operações</div></div></div>
          <div class="risk-item"><div class="m-point" style="background:#fbbf24; color:#0f172a;">R3</div><div><strong>Perda de Especialista Sênior</strong><div style="font-size:11px; color:#64748b;">Impacto Médio · Resp: RH/Gestão</div></div></div>
        </div>
      </div>
    </main></body></html>""",

    # 8. Registro de Riscos
    "registro_riscos.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 8px; }}
    .table th {{ text-align: left; padding: 10px 12px; background: #101c38; color: #94a3b8; font-weight: 700; text-transform: uppercase; font-size: 10px; border-bottom: 2px solid #1a253d; }}
    .table td {{ padding: 12px; border-bottom: 1px solid #14203b; color: #cbd5e1; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">📁</div> Governança</div>
      <div class="nav-group"><div class="nav-title">Compliance</div><div class="nav-link active">📋 Registro</div><div class="nav-link">🛡️ Controles</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Registro Formal de Riscos Operacionais e Estratégicos</h1><p>Inventário completo de eventos, donos de risco, ações preventivas e prazos de revisão</p></div>
        <span class="badge-pill badge-emerald">Auditoria 2025</span>
      </div>
      <div class="card" style="flex:1;">
        <div class="card-head"><h2>📊 Tabela de Riscos Monitorados</h2><span class="badge-pill badge-blue">4 Itens sob Gestão Ativa</span></div>
        <table class="table">
          <thead><tr><th>ID</th><th>Evento de Risco</th><th>Causa Raiz</th><th>Ação de Mitigação</th><th>Responsável</th><th>Status</th></tr></thead>
          <tbody>
            <tr><td><strong>RSK-01</strong></td><td>Indisponibilidade do banco de dados</td><td>Sobrecarga de consultas paralelas</td><td>Implantação de réplica de leitura e cache Redis</td><td>Alexandre (DevOps)</td><td><span class="badge-pill badge-emerald">Em Mitigação</span></td></tr>
            <tr><td><strong>RSK-02</strong></td><td>Erro no cálculo de margem operacional</td><td>Planilhas manuais sem validação</td><td>Migração do cálculo para o sistema automatizado</td><td>Beatriz (Finanças)</td><td><span class="badge-pill badge-blue">Concluído</span></td></tr>
            <tr><td><strong>RSK-03</strong></td><td>Multa por descumprimento de SLA</td><td>Gargalo em triagem de sinistros</td><td>Contratação temporária e automação de alertas</td><td>Carlos (Operação)</td><td><span class="badge-pill badge-amber">Em Atenção</span></td></tr>
            <tr><td><strong>RSK-04</strong></td><td>Vazamento de dados cadastrais</td><td>Falta de autenticação em duas etapas</td><td>Ativação de MFA obrigatório para todos usuários</td><td>Daniel (Segurança)</td><td><span class="badge-pill badge-emerald">Concluído</span></td></tr>
          </tbody>
        </table>
      </div>
    </main></body></html>""",

    # 9. Análise de Impacto da Mudança
    "impacto_mudanca.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid-quad {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; flex: 1; }}
    .quad-box {{ background: #0b1329; border: 1px solid #1a253d; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 10px; }}
    .quad-box h3 {{ font-size: 13px; font-weight: 700; color: #f8fafc; display: flex; align-items: center; justify-content: space-between; }}
    .item-list {{ background: #101c38; border-radius: 8px; padding: 10px 12px; font-size: 12px; color: #94a3b8; border-left: 3px solid #38bdf8; }}
    .item-list.amber {{ border-left-color: #fbbf24; }}
    .item-list.purple {{ border-left-color: #c084fc; }}
    .item-list.green {{ border-left-color: #34d399; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">🔄</div> Mudança</div>
      <div class="nav-group"><div class="nav-title">Gestão</div><div class="nav-link active">🧩 4 Dimensões</div><div class="nav-link">📣 Comunicação</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Matriz de Impacto da Mudança Organizacional</h1><p>Avaliação prévia em Pessoas, Processos, Tecnologia e Clientes para garantir transição suave</p></div>
        <span class="badge-pill badge-blue">Projeto: Novo ERP Operacional</span>
      </div>
      <div class="grid-quad">
        <div class="quad-box">
          <h3>👥 Pessoas & Cultura <span class="badge-pill badge-amber">Impacto Médio</span></h3>
          <div class="item-list amber">Treinamento obrigatório de 16 horas para 45 operadores.</div>
          <div class="item-list amber">Resistência natural à alteração de rotinas consagradas há anos.</div>
          <div class="item-list amber">Necessidade de plano de incentivo para multiplicadores internos.</div>
        </div>
        <div class="quad-box">
          <h3>⚙️ Processos de Negócio <span class="badge-pill badge-rose">Impacto Alto</span></h3>
          <div class="item-list" style="border-left-color:#fb7185;">Redesenho completo do fluxo de entrada de pedidos e faturamento.</div>
          <div class="item-list" style="border-left-color:#fb7185;">Eliminação de 3 etapas manuais de checagem em planilhas.</div>
          <div class="item-list" style="border-left-color:#fb7185;">Revisão de SLAs internos de aprovação entre áreas.</div>
        </div>
        <div class="quad-box">
          <h3>💻 Sistemas & Tecnologia <span class="badge-pill badge-purple">Impacto Alto</span></h3>
          <div class="item-list purple">Integração de 5 bancos legados via barramento seguro de APIs.</div>
          <div class="item-list purple">Período de convivência em paralelo durante 30 dias de validação.</div>
          <div class="item-list purple">Backup contínuo e plano de contingência para reversão rápida.</div>
        </div>
        <div class="quad-box">
          <h3>🤝 Clientes & Fornecedores <span class="badge-pill badge-emerald">Impacto Controlado</span></h3>
          <div class="item-list green">Novo portal de autoatendimento com rastreamento em tempo real.</div>
          <div class="item-list green">Comunicação antecipada de possíveis instabilidades pontuais no fim de semana.</div>
          <div class="item-list green">Canal VIP de suporte telefônico nas 2 primeiras semanas de go-live.</div>
        </div>
      </div>
    </main></body></html>""",

    # 10. Stop Start Continue
    "parar_comecar_continuar.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .columns {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1; }}
    .col-card {{ background: #0b1329; border: 1px solid #1a253d; border-radius: 12px; padding: 18px; display: flex; flex-direction: column; gap: 12px; }}
    .col-head {{ display: flex; align-items: center; justify-content: space-between; padding-bottom: 10px; border-bottom: 2px solid; }}
    .col-head.stop {{ border-color: #fb7185; color: #fb7185; }}
    .col-head.start {{ border-color: #34d399; color: #34d399; }}
    .col-head.continue {{ border-color: #38bdf8; color: #38bdf8; }}
    .col-head h3 {{ font-size: 14px; font-weight: 800; text-transform: uppercase; }}
    .card-note {{ background: #101c38; border-radius: 8px; padding: 12px; font-size: 12.5px; line-height: 1.4; color: #cbd5e1; border: 1px solid #1a253d; display: flex; flex-direction: column; gap: 6px; }}
    .note-votes {{ font-size: 11px; font-weight: 700; color: #94a3b8; align-self: flex-end; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">🔁</div> Melhoria</div>
      <div class="nav-group"><div class="nav-title">Retrospectiva</div><div class="nav-link active">🚦 Parar/Começar</div><div class="nav-link">💡 Ideias</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Retrospectiva Ágil · Parar, Começar e Continuar</h1><p>Alinhamento coletivo sobre o que eliminar, inovar e manter para o próximo ciclo</p></div>
        <span class="badge-pill badge-purple">Sprint Review Mensal</span>
      </div>
      <div class="columns">
        <div class="col-card">
          <div class="col-head stop"><h3>🛑 PARAR</h3><span class="badge-pill badge-rose">Eliminar</span></div>
          <div class="card-note"><span>Reuniões diárias que ultrapassam 25 minutos sem pauta definida.</span><span class="note-votes">👍 9 votos</span></div>
          <div class="card-note"><span>Envio de relatórios em PDF por e-mail em vez de usar o painel online.</span><span class="note-votes">👍 7 votos</span></div>
          <div class="card-note"><span>Aprovação manual de pedidos de baixo valor e baixo risco.</span><span class="note-votes">👍 6 votos</span></div>
        </div>
        <div class="col-card">
          <div class="col-head start"><h3>🚀 COMEÇAR</h3><span class="badge-pill badge-emerald">Inovar</span></div>
          <div class="card-note"><span>Adotar checklist padrão de passagem de plantão entre equipes.</span><span class="note-votes">👍 11 votos</span></div>
          <div class="card-note"><span>Sessão semanal de 30 min de mentoria técnica interna.</span><span class="note-votes">👍 8 votos</span></div>
          <div class="card-note"><span>Automação de alertas críticos no canal do Slack/Teams.</span><span class="note-votes">👍 8 votos</span></div>
        </div>
        <div class="col-card">
          <div class="col-head continue"><h3>⭐ CONTINUAR</h3><span class="badge-pill badge-blue">Manter</span></div>
          <div class="card-note"><span>Transparência nas métricas semanais da diretoria com a equipe.</span><span class="note-votes">👍 12 votos</span></div>
          <div class="card-note"><span>Reconhecimento público de membros que se destacaram no mês.</span><span class="note-votes">👍 10 votos</span></div>
          <div class="card-note"><span>Revisão quinzenal dos planos 30-60-90 dias com os gestores.</span><span class="note-votes">👍 7 votos</span></div>
        </div>
      </div>
    </main></body></html>""",

    # 11. Retrospectiva Pós-Incidente (Post-Mortem)
    "retrospectiva_pos_incidente.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid-pm {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; flex: 1; }}
    .timeline {{ display: flex; flex-direction: column; gap: 10px; position: relative; }}
    .time-event {{ background: #101c38; border-radius: 8px; padding: 11px 14px; font-size: 12px; border-left: 3px solid #38bdf8; display: flex; justify-content: space-between; align-items: center; }}
    .time-event.danger {{ border-left-color: #fb7185; }}
    .time-event.success {{ border-left-color: #34d399; }}
    .five-why {{ background: #101c38; border-radius: 8px; padding: 9px 12px; font-size: 11.5px; margin-bottom: 6px; border-left: 3px solid #fbbf24; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">🔍</div> Incidentes</div>
      <div class="nav-group"><div class="nav-title">Post-Mortem</div><div class="nav-link active">⏱️ Linha do Tempo</div><div class="nav-link">💡 5 Porquês</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Retrospectiva Pós-Incidente · Post-Mortem Sem Culpa</h1><p>Análise de fatores contribuintes, linha cronológica e melhorias sistêmicas preventivas</p></div>
        <span class="badge-pill badge-rose">Severidade: Alta (S1)</span>
      </div>
      <div class="grid-pm">
        <div class="card">
          <div class="card-head"><h2>⏳ Linha Cronológica dos Fatos</h2><span class="badge-pill badge-blue">Duração: 48 Minutos</span></div>
          <div class="timeline">
            <div class="time-event danger"><span><strong>14:02</strong> · Alarme de latência na fila de mensagens ultrapassa 5.000 ms</span><span class="badge-pill badge-rose">Detectado</span></div>
            <div class="time-event"><span><strong>14:10</strong> · Sala de crise aberta com engenharia de infraestrutura e produto</span><span class="badge-pill badge-amber">Mobilização</span></div>
            <div class="time-event"><span><strong>14:25</strong> · Causa identificada: trava em tabela de concorrência após deploy</span><span class="badge-pill badge-purple">Diagnóstico</span></div>
            <div class="time-event success"><span><strong>14:50</strong> · Rollback executado com sucesso e filas normalizadas</span><span class="badge-pill badge-emerald">Resolvido</span></div>
          </div>
        </div>
        <div class="card">
          <div class="card-head"><h2>🧠 Investigação de Causa Raiz (5 Porquês)</h2></div>
          <div class="five-why"><strong>Por quê 1:</strong> A fila travou? Porque o banco entrou em deadlock.</div>
          <div class="five-why"><strong>Por quê 2:</strong> Houve deadlock? Uma migration não rodou em lote.</div>
          <div class="five-why"><strong>Por quê 3:</strong> Não foi em lote? O script manual foi aplicado às pressas.</div>
          <div class="five-why"><strong>Por quê 4:</strong> Foi às pressas? Faltava teste em ambiente de homologação.</div>
          <div class="five-why" style="border-left-color:#34d399;"><strong>Ação Preventiva:</strong> Automação total de deploy com checagem de lock obrigatória no CI/CD.</div>
        </div>
      </div>
    </main></body></html>""",

    # 12. Voz do Cliente (VoC)
    "voz_cliente.jpg": f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
    .grid-voc {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; flex: 1; }}
    .voc-card {{ background: #0b1329; border: 1px solid #1a253d; border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 12px; }}
    .voc-head {{ display: flex; align-items: center; justify-content: space-between; }}
    .voc-head h3 {{ font-size: 13px; font-weight: 700; color: #f8fafc; }}
    .quote-box {{ background: #101c38; border-radius: 8px; padding: 11px; font-size: 12px; color: #cbd5e1; font-style: italic; border-left: 3px solid; }}
    .quote-box.pos {{ border-color: #34d399; }}
    .quote-box.neg {{ border-color: #fb7185; }}
    .quote-author {{ font-size: 10.5px; font-style: normal; color: #64748b; margin-top: 4px; font-weight: 600; }}
    .nps-box {{ display: flex; align-items: center; gap: 16px; background: #101c38; border-radius: 10px; padding: 14px; }}
    .nps-num {{ font-size: 38px; font-weight: 900; color: #34d399; line-height: 1; }}
    </style></head><body>
    <aside>
      <div class="brand"><div class="brand-icon">🗣️</div> Voz do Cliente</div>
      <div class="nav-group"><div class="nav-title">Pesquisa VoC</div><div class="nav-link active">💬 Feedbacks</div><div class="nav-link">📊 NPS Score</div><div class="nav-link">🎯 Planos</div></div>
    </aside>
    <main>
      <div class="top-header">
        <div class="top-title"><h1>Voz do Cliente (VoC) · Análise de Dores e Oportunidades</h1><p>Categorização de comentários, satisfação dos usuários e prioridades de melhoria</p></div>
        <span class="badge-pill badge-emerald">NPS: Zona de Excelência</span>
      </div>
      <div class="grid-voc">
        <div class="voc-card">
          <div class="voc-head"><h3>⚡ Principais Dores & Fricções Identificadas</h3><span class="badge-pill badge-rose">3 Temas Críticos</span></div>
          <div class="quote-box neg">"A emissão de relatórios demora muito quando filtramos mais de 60 dias de dados operacionais."<div class="quote-author">Cliente Corporativo A · Transportadora</div></div>
          <div class="quote-box neg">"Gostaríamos de receber notificações automáticas no WhatsApp para ocorrências de nível grave."<div class="quote-author">Embarcador B · Operações Logísticas</div></div>
        </div>
        <div class="voc-card">
          <div class="voc-head"><h3>🌟 Pontos Fortes Reconhecidos</h3><span class="badge-pill badge-emerald">Diferenciais</span></div>
          <div class="nps-box">
            <div class="nps-num">+78</div>
            <div><strong>Net Promoter Score (NPS)</strong><p style="font-size:11px; color:#94a3b8; margin-top:2px;">92% dos clientes recomendam a plataforma</p></div>
          </div>
          <div class="quote-box pos">"O suporte em tempo real da equipe salvou nossa carga durante a última paralisação."<div class="quote-author">Diretor de Logística · Cliente C</div></div>
        </div>
      </div>
    </main></body></html>"""
}

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    temp_html = os.path.abspath("temp_render.html")
    temp_png = os.path.abspath("temp_render.png")
    
    from PIL import Image
    
    total = len(TEMPLATES)
    for idx, (filename, html) in enumerate(TEMPLATES.items(), 1):
        out_jpg = os.path.join(OUT_DIR, filename)
        with open(temp_html, "w", encoding="utf-8") as f:
            f.write(html)
        
        file_url = "file:///" + temp_html.replace("\\", "/")
        cmd = [
            EDGE_PATH,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1376,768",
            f"--screenshot={temp_png}",
            file_url
        ]
        print(f"[{idx}/{total}] Gerando {filename}...")
        subprocess.run(cmd, check=True)
        
        if os.path.exists(temp_png):
            img = Image.open(temp_png).convert("RGB")
            # Redimensionar se necessário para exatamente 1376x768
            img = img.resize((1376, 768), Image.Resampling.LANCZOS)
            img.save(out_jpg, "JPEG", quality=92, optimize=True)
            os.remove(temp_png)

    if os.path.exists(temp_html):
        os.remove(temp_html)
    print("Todas as 12 imagens foram geradas e convertidas com sucesso!")

if __name__ == "__main__":
    main()
