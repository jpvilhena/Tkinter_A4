/* ── Entity definitions ── */
const ENTITIES = {
  clientes: {
    path: '/clientes',
    idField: 'id_cliente',
    cols: [
      ['id_cliente',       '#'],
      ['nome',             'Nome'],
      ['cpf',              'CPF'],
      ['email',            'Email'],
      ['contato',          'Contato'],
      ['endereco',         'Endereço'],
    ],
    fields: [
      { n: 'nome',             l: 'Nome',              t: 'text',   req: true },
      { n: 'cpf',              l: 'CPF (11 dígitos)',   t: 'text' },
      { n: 'rg',               l: 'RG',                t: 'text' },
      { n: 'email',            l: 'Email',             t: 'text' },
      { n: 'contato',          l: 'Contato',           t: 'text' },
      { n: 'data_nascimento',  l: 'Data de nascimento', t: 'date' },
      { n: 'endereco',         l: 'Endereço',          t: 'text' },
    ],
  },

  caminhoes: {
    path: '/caminhoes',
    idField: 'id_caminhao',
    cols: [
      ['id_caminhao',     '#'],
      ['crlv',            'CRLV'],
      ['ultima_vistoria', 'Última vistoria'],
    ],
    fields: [
      { n: 'crlv',             l: 'CRLV',              t: 'text' },
      { n: 'ultima_vistoria',  l: 'Última vistoria',   t: 'date' },
    ],
  },

  prestadores: {
    path: '/prestadores',
    idField: 'id_prestador',
    cols: [
      ['id_prestador',   '#'],
      ['nome',           'Nome'],
      ['tipo_prestador', 'Tipo'],
      ['cpf',            'CPF'],
      ['cnh',            'CNH'],
      ['email',          'Email'],
    ],
    fields: [
      { n: 'nome',            l: 'Nome',              t: 'text',   req: true },
      { n: 'tipo_prestador',  l: 'Tipo',              t: 'select', opts: ['motorista', 'ajudante', 'outro'] },
      { n: 'cpf',             l: 'CPF (11 dígitos)',  t: 'text' },
      { n: 'rg',              l: 'RG',                t: 'text' },
      { n: 'cnh',             l: 'CNH',               t: 'text' },
      { n: 'email',           l: 'Email',             t: 'text' },
      { n: 'contato',         l: 'Contato',           t: 'text' },
      { n: 'data_nascimento', l: 'Data de nascimento', t: 'date' },
      { n: 'data_admissao',   l: 'Data de admissão',  t: 'date' },
    ],
  },

  servicos: {
    path: '/servicos',
    idField: 'id_servico_oferecido',
    cols: [
      ['id_servico_oferecido', '#'],
      ['nome',                 'Nome'],
      ['preco',                'Preço (R$)'],
      ['requer_ajudante',      'Ajudante?'],
      ['quantidade_caixa_min', 'Cx. mín'],
      ['quantidade_caixa_max', 'Cx. máx'],
    ],
    fields: [
      { n: 'nome',                 l: 'Nome',           t: 'text',   req: true },
      { n: 'preco',                l: 'Preço (R$)',      t: 'number' },
      { n: 'descricao',            l: 'Descrição',      t: 'text' },
      { n: 'requer_ajudante',      l: 'Requer ajudante', t: 'select', opts: ['false', 'true'] },
      { n: 'quantidade_caixa_min', l: 'Qtd caixas mín', t: 'number' },
      { n: 'quantidade_caixa_max', l: 'Qtd caixas máx', t: 'number' },
    ],
  },

  contratos: {
    path: '/contratos',
    idField: 'id_contrato',
    cols: [
      ['id_contrato',        '#'],
      ['id_cliente',         'Cliente ID'],
      ['forma_pagamento',    'Pagamento'],
      ['data_servico',       'Data serviço'],
      ['endereco_origem',    'Origem'],
      ['endereco_destino',   'Destino'],
    ],
    fields: [
      { n: 'id_cliente',           l: 'ID do cliente',      t: 'number', req: true },
      { n: 'id_servico_oferecido', l: 'ID do serviço',      t: 'number' },
      { n: 'forma_pagamento',      l: 'Forma de pagamento', t: 'select', opts: ['pix', 'credito', 'debito', 'dinheiro'] },
      { n: 'quantidade_caixa',     l: 'Qtd de caixas',      t: 'number' },
      { n: 'data_contrato',        l: 'Data do contrato',   t: 'date' },
      { n: 'data_servico',         l: 'Data do serviço',    t: 'date' },
      { n: 'endereco_origem',      l: 'Endereço de origem', t: 'text' },
      { n: 'endereco_destino',     l: 'Endereço de destino', t: 'text' },
    ],
  },

  alocacoes: {
    path: '/alocacoes',
    idField: 'id_alocacao',
    cols: [
      ['id_alocacao',   '#'],
      ['id_contrato',   'Contrato ID'],
      ['id_caminhao',   'Caminhão ID'],
      ['status_servico','Status'],
      ['data_inicio',   'Início'],
      ['data_fim',      'Fim'],
    ],
    fields: [
      { n: 'id_contrato',   l: 'ID do contrato', t: 'number', req: true },
      { n: 'id_caminhao',   l: 'ID do caminhão', t: 'number' },
      { n: 'status_servico',l: 'Status',          t: 'select', opts: ['pendente', 'concluido'] },
      { n: 'data_inicio',   l: 'Data de início',  t: 'date' },
      { n: 'data_fim',      l: 'Data de fim',     t: 'date' },
    ],
  },

  cprestadores: {
    path: '/contrato-prestadores',
    idField: 'id_contrato_prestador',
    cols: [
      ['id_contrato_prestador', '#'],
      ['id_contrato',           'Contrato ID'],
      ['id_prestador',          'Prestador ID'],
      ['funcao',                'Função'],
    ],
    fields: [
      { n: 'id_contrato',  l: 'ID do contrato',  t: 'number', req: true },
      { n: 'id_prestador', l: 'ID do prestador', t: 'number', req: true },
      { n: 'funcao',       l: 'Função',           t: 'select', opts: ['motorista', 'ajudante', 'outro'] },
    ],
  },
};

/* ── State ── */
let currentPage   = 'clientes';
let editingId     = null;
let editingEntity = null;

/* ── API helpers ── */
function apiBase() {
  return document.getElementById('api-base').value.replace(/\/$/, '');
}

async function apiFetch(path, options = {}) {
  const res = await fetch(apiBase() + path, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `HTTP ${res.status}`);
  }
  if (res.status === 204) return null;
  return res.json();
}

/* ── Navigation ── */
function showPage(name) {
  document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n => {
    n.classList.remove('active');
    n.removeAttribute('aria-current');
  });

  document.getElementById('page-' + name).classList.add('active');
  const btn = document.querySelector(`[data-page="${name}"]`);
  if (btn) { btn.classList.add('active'); btn.setAttribute('aria-current', 'page'); }

  currentPage = name;
  loadTable(name);
}

/* ── Table rendering ── */
async function loadTable(name) {
  const e   = ENTITIES[name];
  const el  = document.getElementById('table-' + name);
  el.innerHTML = stateHtml('loading', 'Carregando…');

  try {
    const data = await apiFetch(e.path + '?limit=50');
    if (!data.length) {
      el.innerHTML = stateHtml('empty', 'Nenhum registro encontrado', 'ti-inbox');
      return;
    }
    el.innerHTML = buildTable(e, data);
  } catch (err) {
    el.innerHTML = stateHtml('error', 'Erro ao conectar com a API: ' + err.message, 'ti-wifi-off');
  }
}

function stateHtml(type, msg, icon = '') {
  const cls = type === 'error' ? 'state-msg error' : 'state-msg';
  const ico = icon ? `<i class="ti ${icon}" aria-hidden="true"></i>` : '';
  return `<div class="${cls}">${ico}${msg}</div>`;
}

function buildTable(e, data) {
  const headers = e.cols.map(c => `<th>${c[1]}</th>`).join('') + '<th>Ações</th>';

  const rows = data.map(row => {
    const cells = e.cols.map(([key]) => {
      let v = row[key];

      if (key === 'status_servico') {
        v = `<span class="badge ${v === 'concluido' ? 'badge-done' : 'badge-pending'}">${v ?? '-'}</span>`;
      } else if (key === 'tipo_prestador' || key === 'funcao') {
        const cls = v === 'motorista' ? 'badge-motorista' : v === 'ajudante' ? 'badge-ajudante' : 'badge-outro';
        v = `<span class="badge ${cls}">${v ?? '-'}</span>`;
      } else if (key === 'requer_ajudante') {
        v = v ? '<i class="ti ti-check" style="color:var(--color-success-text)"></i>' : '—';
      } else if (v === null || v === undefined || v === '') {
        v = '<span style="color:var(--color-text-hint)">—</span>';
      }

      return `<td>${v}</td>`;
    }).join('');

    const id = row[e.idField];
    return `
      <tr>
        ${cells}
        <td>
          <div class="actions-cell">
            <button class="btn btn-sm" onclick="openEdit('${currentPage}',${id})" aria-label="Editar registro ${id}">
              <i class="ti ti-edit" aria-hidden="true"></i>
            </button>
            <button class="btn btn-sm btn-danger" onclick="deleteRecord('${currentPage}',${id})" aria-label="Deletar registro ${id}">
              <i class="ti ti-trash" aria-hidden="true"></i>
            </button>
          </div>
        </td>
      </tr>`;
  }).join('');

  return `<table><thead><tr>${headers}</tr></thead><tbody>${rows}</tbody></table>`;
}

/* ── Form building ── */
function buildForm(entityKey, values = {}) {
  const fields = ENTITIES[entityKey].fields;
  const html   = [];

  for (let i = 0; i < fields.length; i += 2) {
    const f1 = fields[i];
    const f2 = fields[i + 1];
    html.push(`<div class="form-row">${fieldHtml(f1, values)}${f2 ? fieldHtml(f2, values) : '<div></div>'}</div>`);
  }

  return html.join('');
}

function fieldHtml(f, values) {
  const raw = values[f.n];
  const val = raw === null || raw === undefined ? '' : raw;

  if (f.t === 'select') {
    const opts = f.opts.map(o =>
      `<option value="${o}" ${String(val) === o ? 'selected' : ''}>${o}</option>`
    ).join('');
    return `
      <div class="form-group">
        <label for="f-${f.n}">${f.l}${f.req ? ' <span aria-hidden="true">*</span>' : ''}</label>
        <select id="f-${f.n}">${opts}</select>
      </div>`;
  }

  return `
    <div class="form-group">
      <label for="f-${f.n}">${f.l}${f.req ? ' <span aria-hidden="true">*</span>' : ''}</label>
      <input type="${f.t}" id="f-${f.n}" value="${val}" ${f.req ? 'required' : ''} />
    </div>`;
}

/* ── Modal ── */
function openCreate(entity) {
  editingId     = null;
  editingEntity = entity;
  document.getElementById('modal-title').textContent = 'Novo registro';
  document.getElementById('modal-body').innerHTML    = buildForm(entity);
  document.getElementById('modal').classList.add('open');
  focusFirstField();
}

async function openEdit(entity, id) {
  editingId     = id;
  editingEntity = entity;
  const e = ENTITIES[entity];

  document.getElementById('modal-title').textContent = `Editar registro #${id}`;
  document.getElementById('modal-body').innerHTML    = stateHtml('loading', 'Carregando…');
  document.getElementById('modal').classList.add('open');

  try {
    const data = await apiFetch(e.path + '/' + id);
    document.getElementById('modal-body').innerHTML = buildForm(entity, data);
  } catch {
    document.getElementById('modal-body').innerHTML = buildForm(entity);
  }

  focusFirstField();
}

function closeModal() {
  document.getElementById('modal').classList.remove('open');
  editingId     = null;
  editingEntity = null;
}

function focusFirstField() {
  setTimeout(() => {
    const first = document.querySelector('#modal-body input, #modal-body select');
    if (first) first.focus();
  }, 50);
}

/* ── Save ── */
async function saveRecord() {
  const e       = ENTITIES[editingEntity];
  const payload = {};

  for (const f of e.fields) {
    const el = document.getElementById('f-' + f.n);
    if (!el) continue;
    const raw = el.value.trim();
    if (raw === '') continue;

    if (f.t === 'number')         payload[f.n] = Number(raw);
    else if (f.n === 'requer_ajudante') payload[f.n] = raw === 'true';
    else                               payload[f.n] = raw;
  }

  const isEdit = editingId !== null;
  const path   = e.path + (isEdit ? '/' + editingId : '');
  const method = isEdit ? 'PATCH' : 'POST';

  try {
    await apiFetch(path, { method, body: JSON.stringify(payload) });
    closeModal();
    showToast(isEdit ? 'Atualizado com sucesso' : 'Criado com sucesso');
    loadTable(editingEntity);
  } catch (err) {
    showToast('Erro: ' + err.message, true);
  }
}

/* ── Delete ── */
async function deleteRecord(entity, id) {
  if (!confirm(`Deletar registro #${id}? Esta ação não pode ser desfeita.`)) return;
  const e = ENTITIES[entity];

  try {
    await apiFetch(e.path + '/' + id, { method: 'DELETE' });
    showToast('Registro deletado');
    loadTable(entity);
  } catch (err) {
    showToast('Erro: ' + err.message, true);
  }
}

/* ── Toast ── */
let toastTimer = null;

function showToast(msg, isError = false) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className   = 'toast show ' + (isError ? 'toast-error' : 'toast-success');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => t.classList.remove('show'), 3200);
}

/* ── Bootstrap ── */
document.addEventListener('DOMContentLoaded', () => {
  /* Nav buttons */
  document.querySelectorAll('.nav-item[data-page]').forEach(btn => {
    btn.addEventListener('click', () => showPage(btn.dataset.page));
  });

  /* Create buttons */
  document.querySelectorAll('[data-create]').forEach(btn => {
    btn.addEventListener('click', () => openCreate(btn.dataset.create));
  });

  /* Modal close */
  document.getElementById('modal').addEventListener('click', e => {
    if (e.target === document.getElementById('modal')) closeModal();
  });
  document.getElementById('modal-cancel').addEventListener('click', closeModal);
  document.getElementById('modal-save').addEventListener('click', saveRecord);

  /* Close modal on Escape */
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape' && document.getElementById('modal').classList.contains('open')) {
      closeModal();
    }
  });

  /* Load initial page */
  showPage('clientes');
});