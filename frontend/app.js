/* =============================================================
   Entity definitions
   Each entity describes how to display and edit a resource from the API.

   Properties:
     path        – API endpoint path (appended to the base URL)
     idField     – name of the primary-key field returned by the API
     columns     – pairs of [fieldName, displayLabel] shown in the table
     fields      – form fields, each with:
                     name     – matches the API field name
                     label    – human-readable label shown on screen
                     type     – HTML input type, or 'select'
                     required – if true, the field is marked required
                     options  – list of allowed values (only for 'select')
   ============================================================= */

const ENTITIES = {
  clientes: {
    path: '/clientes',
    idField: 'id_cliente',
    columns: [
      ['id_cliente', '#'],
      ['nome',       'Nome'],
      ['cpf',        'CPF'],
      ['email',      'Email'],
      ['contato',    'Contato'],
      ['endereco',   'Endereço'],
    ],
    fields: [
      { name: 'nome',            label: 'Nome',               type: 'text',   required: true },
      { name: 'cpf',             label: 'CPF (11 dígitos)',   type: 'text' },
      { name: 'rg',              label: 'RG',                 type: 'text' },
      { name: 'email',           label: 'Email',              type: 'text' },
      { name: 'contato',         label: 'Contato',            type: 'text' },
      { name: 'data_nascimento', label: 'Data de nascimento', type: 'date' },
      { name: 'endereco',        label: 'Endereço',           type: 'text' },
    ],
  },

  caminhoes: {
    path: '/caminhoes',
    idField: 'id_caminhao',
    columns: [
      ['id_caminhao',     '#'],
      ['crlv',            'CRLV'],
      ['ultima_vistoria', 'Última vistoria'],
    ],
    fields: [
      { name: 'crlv',            label: 'CRLV',            type: 'text' },
      { name: 'ultima_vistoria', label: 'Última vistoria', type: 'date' },
    ],
  },

  prestadores: {
    path: '/prestadores',
    idField: 'id_prestador',
    columns: [
      ['id_prestador',   '#'],
      ['nome',           'Nome'],
      ['tipo_prestador', 'Tipo'],
      ['cpf',            'CPF'],
      ['cnh',            'CNH'],
      ['email',          'Email'],
    ],
    fields: [
      { name: 'nome',            label: 'Nome',               type: 'text',   required: true },
      { name: 'tipo_prestador',  label: 'Tipo',               type: 'select', options: ['motorista', 'ajudante', 'outro'] },
      { name: 'cpf',             label: 'CPF (11 dígitos)',   type: 'text' },
      { name: 'rg',              label: 'RG',                 type: 'text' },
      { name: 'cnh',             label: 'CNH',                type: 'text' },
      { name: 'email',           label: 'Email',              type: 'text' },
      { name: 'contato',         label: 'Contato',            type: 'text' },
      { name: 'data_nascimento', label: 'Data de nascimento', type: 'date' },
      { name: 'data_admissao',   label: 'Data de admissão',   type: 'date' },
    ],
  },

  servicos: {
    path: '/servicos',
    idField: 'id_servico_oferecido',
    columns: [
      ['id_servico_oferecido', '#'],
      ['nome',                 'Nome'],
      ['preco',                'Preço (R$)'],
      ['requer_ajudante',      'Ajudante?'],
      ['quantidade_caixa_min', 'Cx. mín'],
      ['quantidade_caixa_max', 'Cx. máx'],
    ],
    fields: [
      { name: 'nome',                 label: 'Nome',            type: 'text',   required: true },
      { name: 'preco',                label: 'Preço (R$)',      type: 'number' },
      { name: 'descricao',            label: 'Descrição',       type: 'text' },
      { name: 'requer_ajudante',      label: 'Requer ajudante', type: 'select', options: ['false', 'true'] },
      { name: 'quantidade_caixa_min', label: 'Qtd caixas mín', type: 'number' },
      { name: 'quantidade_caixa_max', label: 'Qtd caixas máx', type: 'number' },
    ],
  },

  contratos: {
    path: '/contratos',
    idField: 'id_contrato',
    columns: [
      ['id_contrato',      '#'],
      ['id_cliente',       'Cliente ID'],
      ['forma_pagamento',  'Pagamento'],
      ['data_servico',     'Data serviço'],
      ['endereco_origem',  'Origem'],
      ['endereco_destino', 'Destino'],
    ],
    fields: [
      { name: 'id_cliente',           label: 'ID do cliente',       type: 'number', required: true },
      { name: 'id_servico_oferecido', label: 'ID do serviço',       type: 'number' },
      { name: 'forma_pagamento',      label: 'Forma de pagamento',  type: 'select', options: ['pix', 'credito', 'debito', 'dinheiro'] },
      { name: 'quantidade_caixa',     label: 'Qtd de caixas',       type: 'number' },
      { name: 'data_contrato',        label: 'Data do contrato',    type: 'date' },
      { name: 'data_servico',         label: 'Data do serviço',     type: 'date' },
      { name: 'endereco_origem',      label: 'Endereço de origem',  type: 'text' },
      { name: 'endereco_destino',     label: 'Endereço de destino', type: 'text' },
    ],
  },

  alocacoes: {
    path: '/alocacoes',
    idField: 'id_alocacao',
    columns: [
      ['id_alocacao',    '#'],
      ['id_contrato',    'Contrato ID'],
      ['id_caminhao',    'Caminhão ID'],
      ['status_servico', 'Status'],
      ['data_inicio',    'Início'],
      ['data_fim',       'Fim'],
    ],
    fields: [
      { name: 'id_contrato',    label: 'ID do contrato', type: 'number', required: true },
      { name: 'id_caminhao',    label: 'ID do caminhão', type: 'number' },
      { name: 'status_servico', label: 'Status',         type: 'select', options: ['pendente', 'concluido'] },
      { name: 'data_inicio',    label: 'Data de início', type: 'date' },
      { name: 'data_fim',       label: 'Data de fim',    type: 'date' },
    ],
  },

  cprestadores: {
    path: '/contrato-prestadores',
    idField: 'id_contrato_prestador',
    columns: [
      ['id_contrato_prestador', '#'],
      ['id_contrato',           'Contrato ID'],
      ['id_prestador',          'Prestador ID'],
      ['funcao',                'Função'],
    ],
    fields: [
      { name: 'id_contrato',  label: 'ID do contrato',  type: 'number', required: true },
      { name: 'id_prestador', label: 'ID do prestador', type: 'number', required: true },
      { name: 'funcao',       label: 'Função',           type: 'select', options: ['motorista', 'ajudante', 'outro'] },
    ],
  },
};


/* =============================================================
   App state
   ============================================================= */

let currentPage    = 'clientes';  // key of the currently visible entity
let editingId      = null;        // ID of the record being edited (null when creating)
let editingEntity  = null;        // entity key of the open modal


/* =============================================================
   API helpers
   ============================================================= */

const API_BASE_URL = 'http://localhost:8000';

/**
 * Wraps fetch() with JSON headers, error handling, and base-URL prefix.
 * Throws a descriptive Error if the response is not 2xx.
 */
async function apiFetch(path, options = {}) {
  // Only send Content-Type on requests that actually have a body.
  // Sending it on GET/DELETE requests can cause FastAPI to return 422.
  const headers = options.body !== undefined
    ? { 'Content-Type': 'application/json' }
    : {};

  const response = await fetch(API_BASE_URL + path, {
    ...options,
    headers,
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody.detail || `HTTP ${response.status}`);
  }

  // 204 No Content – DELETE responses have no body to parse
  if (response.status === 204) return null;

  return response.json();
}


/* =============================================================
   Navigation
   ============================================================= */

/**
 * Activates the page matching the given entity key,
 * highlights its nav button, and loads the table data.
 */
function showPage(entityKey) {
  document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(navButton => {
    navButton.classList.remove('active');
    navButton.removeAttribute('aria-current');
  });

  document.getElementById('page-' + entityKey).classList.add('active');

  const activeNavButton = document.querySelector(`[data-page="${entityKey}"]`);
  if (activeNavButton) {
    activeNavButton.classList.add('active');
    activeNavButton.setAttribute('aria-current', 'page');
  }

  currentPage = entityKey;
  loadTable(entityKey);
}


/* =============================================================
   Table rendering
   ============================================================= */

/**
 * Fetches records from the API and renders them as a table
 * inside the container for the given entity.
 */
async function loadTable(entityKey) {
  const entity    = ENTITIES[entityKey];
  const container = document.getElementById('table-' + entityKey);

  container.innerHTML = buildStateMessage('loading', 'Carregando…');

  try {
    const records = await apiFetch(entity.path + '?limit=50');

    if (!records.length) {
      container.innerHTML = buildStateMessage('empty', 'Nenhum registro encontrado', 'ti-inbox');
      return;
    }

    container.innerHTML = buildTable(entity, records, entityKey);
  } catch (error) {
    container.innerHTML = buildStateMessage('error', 'Erro ao conectar com a API: ' + error.message, 'ti-wifi-off');
  }
}

/**
 * Returns an HTML string for loading / empty / error states.
 */
function buildStateMessage(type, message, iconClass = '') {
  const cssClass  = type === 'error' ? 'state-msg error' : 'state-msg';
  const iconHtml  = iconClass ? `<i class="ti ${iconClass}" aria-hidden="true"></i>` : '';
  return `<div class="${cssClass}">${iconHtml}${message}</div>`;
}

/**
 * Builds the full <table> HTML for a list of records.
 */
function buildTable(entity, records, entityKey) {
  const headerCells = entity.columns
    .map(([, label]) => `<th>${label}</th>`)
    .join('') + '<th>Ações</th>';

  const bodyRows = records.map(record => buildTableRow(entity, record, entityKey)).join('');

  return `<table><thead><tr>${headerCells}</tr></thead><tbody>${bodyRows}</tbody></table>`;
}

/**
 * Builds a single <tr> for one record, including the action buttons.
 */
function buildTableRow(entity, record, entityKey) {
  const cells = entity.columns.map(([fieldName]) => {
    const rawValue = record[fieldName];
    const cellContent = formatCellValue(fieldName, rawValue);
    return `<td>${cellContent}</td>`;
  }).join('');

  const recordId = record[entity.idField];

  return `
    <tr>
      ${cells}
      <td>
        <div class="actions-cell">
          <button class="btn btn-sm" onclick="openEdit('${entityKey}', ${recordId})" aria-label="Editar registro ${recordId}">
            <i class="ti ti-edit" aria-hidden="true"></i>
          </button>
          <button class="btn btn-sm btn-danger" onclick="deleteRecord('${entityKey}', ${recordId})" aria-label="Deletar registro ${recordId}">
            <i class="ti ti-trash" aria-hidden="true"></i>
          </button>
        </div>
      </td>
    </tr>`;
}

/**
 * Converts a raw field value into display HTML.
 * Handles special fields (status, type badges, booleans) and null values.
 */
function formatCellValue(fieldName, value) {
  if (fieldName === 'status_servico') {
    const badgeClass = value === 'concluido' ? 'badge-done' : 'badge-pending';
    return `<span class="badge ${badgeClass}">${value ?? '-'}</span>`;
  }

  if (fieldName === 'tipo_prestador' || fieldName === 'funcao') {
    const badgeClass =
      value === 'motorista' ? 'badge-motorista' :
      value === 'ajudante'  ? 'badge-ajudante'  :
                              'badge-outro';
    return `<span class="badge ${badgeClass}">${value ?? '-'}</span>`;
  }

  if (fieldName === 'requer_ajudante') {
    return value
      ? '<i class="ti ti-check" style="color:var(--color-success-text)"></i>'
      : '—';
  }

  if (value === null || value === undefined || value === '') {
    return '<span style="color:var(--color-text-hint)">—</span>';
  }

  return value;
}


/* =============================================================
   Form building
   ============================================================= */

/**
 * Renders all form fields for an entity, grouped two per row.
 * Existing values (when editing) are pre-filled via the `values` object.
 */
function buildForm(entityKey, values = {}) {
  const fields    = ENTITIES[entityKey].fields;
  const rowBlocks = [];

  for (let index = 0; index < fields.length; index += 2) {
    const leftField  = fields[index];
    const rightField = fields[index + 1];

    rowBlocks.push(`
      <div class="form-row">
        ${buildFieldHtml(leftField, values)}
        ${rightField ? buildFieldHtml(rightField, values) : '<div></div>'}
      </div>
    `);
  }

  return rowBlocks.join('');
}

/**
 * Returns the HTML for a single form field (input or select).
 */
function buildFieldHtml(field, values) {
  const rawValue     = values[field.name];
  const currentValue = rawValue === null || rawValue === undefined ? '' : rawValue;
  const requiredMark = field.required ? ' <span aria-hidden="true">*</span>' : '';

  if (field.type === 'select') {
    const optionElements = field.options.map(option => `
      <option value="${option}" ${String(currentValue) === option ? 'selected' : ''}>
        ${option}
      </option>
    `).join('');

    return `
      <div class="form-group">
        <label for="field-${field.name}">${field.label}${requiredMark}</label>
        <select id="field-${field.name}">${optionElements}</select>
      </div>`;
  }

  return `
    <div class="form-group">
      <label for="field-${field.name}">${field.label}${requiredMark}</label>
      <input
        type="${field.type}"
        id="field-${field.name}"
        value="${currentValue}"
        ${field.required ? 'required' : ''}
      />
    </div>`;
}


/* =============================================================
   Modal
   ============================================================= */

/** Opens the modal in "create new record" mode. */
function openCreate(entityKey) {
  editingId     = null;
  editingEntity = entityKey;

  document.getElementById('modal-title').textContent = 'Novo registro';
  document.getElementById('modal-body').innerHTML    = buildForm(entityKey);
  document.getElementById('modal').classList.add('open');

  focusFirstField();
}

/** Opens the modal in "edit existing record" mode, loading current values from the API. */
async function openEdit(entityKey, recordId) {
  editingId     = recordId;
  editingEntity = entityKey;

  const entity = ENTITIES[entityKey];

  document.getElementById('modal-title').textContent = `Editar registro #${recordId}`;
  document.getElementById('modal-body').innerHTML    = buildStateMessage('loading', 'Carregando…');
  document.getElementById('modal').classList.add('open');

  try {
    const currentValues = await apiFetch(entity.path + '/' + recordId);
    document.getElementById('modal-body').innerHTML = buildForm(entityKey, currentValues);
  } catch {
    // If loading fails, still show the empty form so the user can try manually
    document.getElementById('modal-body').innerHTML = buildForm(entityKey);
  }

  focusFirstField();
}

/** Closes the modal and resets editing state. */
function closeModal() {
  document.getElementById('modal').classList.remove('open');
  editingId     = null;
  editingEntity = null;
}

/** Moves focus to the first interactive field inside the modal. */
function focusFirstField() {
  setTimeout(() => {
    const firstField = document.querySelector('#modal-body input, #modal-body select');
    if (firstField) firstField.focus();
  }, 50);
}


/* =============================================================
   Save / Delete
   ============================================================= */

/**
 * Reads all form fields, builds a typed payload, and sends it
 * to the API as either PATCH (edit) or POST (create).
 */
async function saveRecord() {
  const entity  = ENTITIES[editingEntity];
  const payload = {};

  for (const field of entity.fields) {
    const inputElement = document.getElementById('field-' + field.name);
    if (!inputElement) continue;

    const rawValue = inputElement.value.trim();

    // For selects, an empty string means "no option chosen" — skip it.
    // For text/number/date inputs, empty also means the user left it blank — skip it.
    if (rawValue === '') continue;

    if (field.type === 'number') {
      // The API expects a number, not the string "42"
      payload[field.name] = Number(rawValue);
    } else if (field.type === 'select' && field.options?.every(o => o === 'true' || o === 'false')) {
      // A select whose only options are 'true'/'false' represents a boolean field.
      // Send the actual boolean, not the string.
      payload[field.name] = rawValue === 'true';
    } else {
      payload[field.name] = rawValue;
    }
  }

  const isEditing  = editingId !== null;
  const apiPath    = entity.path + (isEditing ? '/' + editingId : '');
  const httpMethod = isEditing ? 'PATCH' : 'POST';

  try {
    await apiFetch(apiPath, { method: httpMethod, body: JSON.stringify(payload) });
    closeModal();
    showToast(isEditing ? 'Atualizado com sucesso' : 'Criado com sucesso');
    loadTable(editingEntity);
  } catch (error) {
    showToast('Erro: ' + error.message, true);
  }
}

/**
 * Asks for confirmation, then deletes the record via the API.
 */
async function deleteRecord(entityKey, recordId) {
  const confirmed = confirm(`Deletar registro #${recordId}? Esta ação não pode ser desfeita.`);
  if (!confirmed) return;

  const entity = ENTITIES[entityKey];

  try {
    await apiFetch(entity.path + '/' + recordId, { method: 'DELETE' });
    showToast('Registro deletado');
    loadTable(entityKey);
  } catch (error) {
    showToast('Erro: ' + error.message, true);
  }
}


/* =============================================================
   Toast notifications
   ============================================================= */

let toastDismissTimer = null;

/**
 * Shows a brief notification at the bottom of the screen.
 * Pass isError = true to show it in the error style.
 */
function showToast(message, isError = false) {
  const toastElement = document.getElementById('toast');
  toastElement.textContent = message;
  toastElement.className   = 'toast show ' + (isError ? 'toast-error' : 'toast-success');

  clearTimeout(toastDismissTimer);
  toastDismissTimer = setTimeout(() => toastElement.classList.remove('show'), 3200);
}


/* =============================================================
   Bootstrap – wire up all static event listeners on load
   ============================================================= */

document.addEventListener('DOMContentLoaded', () => {

  // Sidebar navigation buttons
  document.querySelectorAll('.nav-item[data-page]').forEach(navButton => {
    navButton.addEventListener('click', () => showPage(navButton.dataset.page));
  });

  // "New record" buttons scattered across each page
  document.querySelectorAll('[data-create]').forEach(createButton => {
    createButton.addEventListener('click', () => openCreate(createButton.dataset.create));
  });

  // Close modal by clicking the backdrop
  document.getElementById('modal').addEventListener('click', event => {
    if (event.target === document.getElementById('modal')) closeModal();
  });

  // Modal footer buttons
  document.getElementById('modal-cancel').addEventListener('click', closeModal);
  document.getElementById('modal-save').addEventListener('click', saveRecord);

  // Close modal with Escape key
  document.addEventListener('keydown', event => {
    const modalIsOpen = document.getElementById('modal').classList.contains('open');
    if (event.key === 'Escape' && modalIsOpen) closeModal();
  });

  // Show the first page on load
  showPage('clientes');
});