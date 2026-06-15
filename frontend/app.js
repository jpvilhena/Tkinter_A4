/* ====================================
   MUDAEXPRESS - FRONTEND JAVASCRIPT
   Lógica de comunicação com o backend
   ==================================== */

// Configuração da API - MUDE ESTE ENDEREÇO SE SEU BACKEND ESTIVER EM OUTRO LOCAL
const API_BASE_URL = 'http://localhost:8000';

// ====================================
// FUNÇÕES DE UTILITÁRIOS
// ====================================

/**
 * Alterna entre abas (tabs) da aplicação
 * @param {string} tabName - Nome da aba a exibir
 */
function switchTab(tabName) {
    // Oculta todas as abas
    const allTabs = document.querySelectorAll('.tab-content');
    allTabs.forEach(tab => tab.classList.remove('active'));

    // Remove a classe 'active' de todos os botões de navegação
    const allNavBtns = document.querySelectorAll('.nav-btn');
    allNavBtns.forEach(btn => btn.classList.remove('active'));

    // Mostra a aba selecionada e marca seu botão como ativo
    document.getElementById(tabName).classList.add('active');
    event.target.classList.add('active');

    // Carrega os dados da aba selecionada
    if (tabName === 'clients') {
        loadClients();
    } else if (tabName === 'drivers') {
        loadDrivers();
    } else if (tabName === 'trucks') {
        loadTrucks();
    } else if (tabName === 'helpers') {
        loadHelpers();
    } else if (tabName === 'services') {
        loadServices();
        loadClientsForSelect();
        loadTrucksCheckbox();
        loadDriversCheckbox();
        loadHelpersCheckbox();
    }
}

/**
 * Exibe uma mensagem de alerta na tela
 * @param {string} message - Mensagem a exibir
 * @param {string} type - Tipo de alerta: 'success' ou 'error'
 */
function showAlert(message, type = 'success') {
    const alertContainer = document.getElementById('alertContainer');
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    alertContainer.appendChild(alertDiv);

    // Remove o alerta após 4 segundos
    setTimeout(() => {
        alertDiv.remove();
    }, 4000);
}

/**
 * Realiza chamadas à API do backend
 * @param {string} endpoint - Caminho do endpoint (ex: '/clients')
 * @param {string} method - Método HTTP (GET, POST, PUT, DELETE)
 * @param {object} data - Dados a enviar (para POST/PUT)
 * @returns {Promise} - Promise com a resposta da API
 */
async function apiCall(endpoint, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };

        // Adiciona o corpo da requisição para POST/PUT
        if (data) {
            options.body = JSON.stringify(data);
        }

        const response = await fetch(`${API_BASE_URL}${endpoint}`, options);
        
        console.log(`${API_BASE_URL}${endpoint}`, options)
        // Verifica se a resposta foi bem-sucedida
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || `Erro na requisição: ${response.status}`);
        }

        // Para DELETE, a resposta pode estar vazia
        if (method === 'DELETE') {
            return { ok: true };
        }

        return await response.json();
    } catch (error) {
        console.error('Erro na API:', error);
        showAlert(`Erro: ${error.message}`, 'error');
        throw error;
    }
}

/**
 * Abre o modal de edição
 * @param {string} title - Título do modal
 */
function openModal(title) {
    document.getElementById('editModal').style.display = 'block';
    document.getElementById('modalTitle').textContent = title;
}

/**
 * Fecha o modal de edição
 */
function closeModal() {
    document.getElementById('editModal').style.display = 'none';
    document.getElementById('editForm').innerHTML = '';
}

// Fecha o modal quando clica fora dele
window.onclick = function(event) {
    const modal = document.getElementById('editModal');
    if (event.target === modal) {
        closeModal();
    }
}

// ====================================
// FUNÇÕES DE CLIENTES
// ====================================

/**
 * Carrega a lista de clientes da API e exibe na tela
 */
async function loadClients() {
    try {
        const clients = await apiCall('/clients');
        const clientsList = document.getElementById('clientsList');

        // Limpa a lista
        clientsList.innerHTML = '';

        // Se não houver clientes, exibe mensagem
        if (clients.length === 0) {
            clientsList.innerHTML = '<div class="empty-state"><p>Nenhum cliente cadastrado</p></div>';
            return;
        }

        // Exibe cada cliente em um card
        clients.forEach(client => {
            const card = document.createElement('div');
            card.className = 'item-card';
            card.innerHTML = `
                <div class="item-info">
                    <h4>${client.name}</h4>
                    <p><strong>Email:</strong> ${client.email || 'N/A'}</p>
                    <p><strong>Telefone:</strong> ${client.phone || 'N/A'}</p>
                    <p><strong>Endereço:</strong> ${client.address || 'N/A'}</p>
                </div>
                <div class="item-actions">
                    <button class="btn btn-success" onclick="editClient(${client.id})">Editar</button>
                    <button class="btn btn-danger" onclick="deleteClient(${client.id})">Deletar</button>
                </div>
            `;
            clientsList.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar clientes:', error);
    }
}

/**
 * Cria um novo cliente via formulário
 */
async function createClient(event) {
    event.preventDefault();

    // Coleta os dados do formulário
    const clientData = {
        name: document.getElementById('clientName').value,
        email: document.getElementById('clientEmail').value,
        phone: document.getElementById('clientPhone').value,
        address: document.getElementById('clientAddress').value
    };

    try {
        await apiCall('/clients', 'POST', clientData);
        showAlert('Cliente cadastrado com sucesso!', 'success');

        // Limpa o formulário
        event.target.reset();

        // Recarrega a lista de clientes
        loadClients();
    } catch (error) {
        console.error('Erro ao criar cliente:', error);
    }
}

/**
 * Edita um cliente existente
 */
function editClient(clientId) {
    // Implementação simplificada - pode ser expandida
    alert('Funcionalidade de edição em desenvolvimento');
}

/**
 * Deleta um cliente
 */
async function deleteClient(clientId) {
    if (!confirm('Tem certeza que deseja deletar este cliente?')) {
        return;
    }

    try {
        await apiCall(`/clients/${clientId}`, 'DELETE');
        showAlert('Cliente deletado com sucesso!', 'success');
        loadClients();
    } catch (error) {
        console.error('Erro ao deletar cliente:', error);
    }
}

// ====================================
// FUNÇÕES DE MOTORISTAS
// ====================================

/**
 * Carrega a lista de motoristas da API e exibe na tela
 */
async function loadDrivers() {
    try {
        const drivers = await apiCall('/drivers');
        const driversList = document.getElementById('driversList');

        driversList.innerHTML = '';

        if (drivers.length === 0) {
            driversList.innerHTML = '<div class="empty-state"><p>Nenhum motorista cadastrado</p></div>';
            return;
        }

        drivers.forEach(driver => {
            const card = document.createElement('div');
            card.className = 'item-card';
            card.innerHTML = `
                <div class="item-info">
                    <h4>${driver.name}</h4>
                    <p><strong>CPF:</strong> ${driver.cpf || 'N/A'}</p>
                    <p><strong>Habilitação:</strong> ${driver.license}</p>
                    <p><strong>Telefone:</strong> ${driver.phone || 'N/A'}</p>
                </div>
                <div class="item-actions">
                    <button class="btn btn-success" onclick="editDriver(${driver.id})">Editar</button>
                    <button class="btn btn-danger" onclick="deleteDriver(${driver.id})">Deletar</button>
                </div>
            `;
            driversList.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar motoristas:', error);
    }
}

/**
 * Cria um novo motorista via formulário
 */
async function createDriver(event) {
    event.preventDefault();

    const driverData = {
        name: document.getElementById('driverName').value,
        cpf: document.getElementById('driverCPF').value,
        license: document.getElementById('driverLicense').value,
        phone: document.getElementById('driverPhone').value
    };

    try {
        await apiCall('/drivers', 'POST', driverData);
        showAlert('Motorista cadastrado com sucesso!', 'success');
        event.target.reset();
        loadDrivers();
    } catch (error) {
        console.error('Erro ao criar motorista:', error);
    }
}

/**
 * Edita um motorista existente
 */
function editDriver(driverId) {
    alert('Funcionalidade de edição em desenvolvimento');
}

/**
 * Deleta um motorista
 */
async function deleteDriver(driverId) {
    if (!confirm('Tem certeza que deseja deletar este motorista?')) {
        return;
    }

    try {
        await apiCall(`/drivers/${driverId}`, 'DELETE');
        showAlert('Motorista deletado com sucesso!', 'success');
        loadDrivers();
    } catch (error) {
        console.error('Erro ao deletar motorista:', error);
    }
}

// Carrega motoristas para o checkbox na aba de serviços
async function loadDriversCheckbox() {
    try {
        const drivers = await apiCall('/drivers');
        const driversCheckbox = document.getElementById('driversCheckbox');
        driversCheckbox.innerHTML = '';

        drivers.forEach(driver => {
            const label = document.createElement('label');
            label.className = 'checkbox-item';
            label.innerHTML = `
                <input type="checkbox" value="${driver.id}" class="driver-checkbox">
                <span>${driver.name}</span>
            `;
            driversCheckbox.appendChild(label);
        });
    } catch (error) {
        console.error('Erro ao carregar motoristas para checkbox:', error);
    }
}

// ====================================
// FUNÇÕES DE CAMINHÕES
// ====================================

/**
 * Carrega a lista de caminhões da API e exibe na tela
 */
async function loadTrucks() {
    try {
        const trucks = await apiCall('/trucks');
        const trucksList = document.getElementById('trucksList');

        trucksList.innerHTML = '';

        if (trucks.length === 0) {
            trucksList.innerHTML = '<div class="empty-state"><p>Nenhum caminhão cadastrado</p></div>';
            return;
        }

        trucks.forEach(truck => {
            const card = document.createElement('div');
            card.className = 'item-card';
            card.innerHTML = `
                <div class="item-info">
                    <h4>Placa: ${truck.plate}</h4>
                    <p><strong>Modelo:</strong> ${truck.model || 'N/A'}</p>
                    <p><strong>Capacidade:</strong> ${truck.capacity || 'N/A'}</p>
                    <p><strong>Observações:</strong> ${truck.notes || 'N/A'}</p>
                </div>
                <div class="item-actions">
                    <button class="btn btn-success" onclick="editTruck(${truck.id})">Editar</button>
                    <button class="btn btn-danger" onclick="deleteTruck(${truck.id})">Deletar</button>
                </div>
            `;
            trucksList.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar caminhões:', error);
    }
}

/**
 * Cria um novo caminhão via formulário
 */
async function createTruck(event) {
    event.preventDefault();

    const truckData = {
        plate: document.getElementById('truckPlate').value,
        model: document.getElementById('truckModel').value,
        capacity: document.getElementById('truckCapacity').value,
        notes: document.getElementById('truckNotes').value || null
    };

    try {
        await apiCall('/trucks', 'POST', truckData);
        showAlert('Caminhão cadastrado com sucesso!', 'success');
        event.target.reset();
        loadTrucks();
    } catch (error) {
        console.error('Erro ao criar caminhão:', error);
    }
}

/**
 * Edita um caminhão existente
 */
function editTruck(truckId) {
    alert('Funcionalidade de edição em desenvolvimento');
}

/**
 * Deleta um caminhão
 */
async function deleteTruck(truckId) {
    if (!confirm('Tem certeza que deseja deletar este caminhão?')) {
        return;
    }

    try {
        await apiCall(`/trucks/${truckId}`, 'DELETE');
        showAlert('Caminhão deletado com sucesso!', 'success');
        loadTrucks();
    } catch (error) {
        console.error('Erro ao deletar caminhão:', error);
    }
}

// Carrega caminhões para o checkbox na aba de serviços
async function loadTrucksCheckbox() {
    try {
        const trucks = await apiCall('/trucks');
        const trucksCheckbox = document.getElementById('trucksCheckbox');
        trucksCheckbox.innerHTML = '';

        trucks.forEach(truck => {
            const label = document.createElement('label');
            label.className = 'checkbox-item';
            label.innerHTML = `
                <input type="checkbox" value="${truck.id}" class="truck-checkbox">
                <span>${truck.plate} - ${truck.model || 'N/A'}</span>
            `;
            trucksCheckbox.appendChild(label);
        });
    } catch (error) {
        console.error('Erro ao carregar caminhões para checkbox:', error);
    }
}

// ====================================
// FUNÇÕES DE AJUDANTES
// ====================================

/**
 * Carrega a lista de ajudantes da API e exibe na tela
 */
async function loadHelpers() {
    try {
        const helpers = await apiCall('/helpers');
        const helpersList = document.getElementById('helpersList');

        helpersList.innerHTML = '';

        if (helpers.length === 0) {
            helpersList.innerHTML = '<div class="empty-state"><p>Nenhum ajudante cadastrado</p></div>';
            return;
        }

        helpers.forEach(helper => {
            const card = document.createElement('div');
            card.className = 'item-card';
            card.innerHTML = `
                <div class="item-info">
                    <h4>${helper.name}</h4>
                    <p><strong>Telefone:</strong> ${helper.phone || 'N/A'}</p>
                    <p><strong>Diária:</strong> ${helper.daily_rate || 'N/A'}</p>
                </div>
                <div class="item-actions">
                    <button class="btn btn-success" onclick="editHelper(${helper.id})">Editar</button>
                    <button class="btn btn-danger" onclick="deleteHelper(${helper.id})">Deletar</button>
                </div>
            `;
            helpersList.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar ajudantes:', error);
    }
}

/**
 * Cria um novo ajudante via formulário
 */
async function createHelper(event) {
    event.preventDefault();

    const helperData = {
        name: document.getElementById('helperName').value,
        phone: document.getElementById('helperPhone').value,
        daily_rate: document.getElementById('helperDailyRate').value
    };

    try {
        await apiCall('/helpers', 'POST', helperData);
        showAlert('Ajudante cadastrado com sucesso!', 'success');
        event.target.reset();
        loadHelpers();
    } catch (error) {
        console.error('Erro ao criar ajudante:', error);
    }
}

/**
 * Edita um ajudante existente
 */
function editHelper(helperId) {
    alert('Funcionalidade de edição em desenvolvimento');
}

/**
 * Deleta um ajudante
 */
async function deleteHelper(helperId) {
    if (!confirm('Tem certeza que deseja deletar este ajudante?')) {
        return;
    }

    try {
        await apiCall(`/helpers/${helperId}`, 'DELETE');
        showAlert('Ajudante deletado com sucesso!', 'success');
        loadHelpers();
    } catch (error) {
        console.error('Erro ao deletar ajudante:', error);
    }
}

// Carrega ajudantes para o checkbox na aba de serviços
async function loadHelpersCheckbox() {
    try {
        const helpers = await apiCall('/helpers');
        const helpersCheckbox = document.getElementById('helpersCheckbox');
        helpersCheckbox.innerHTML = '';

        helpers.forEach(helper => {
            const label = document.createElement('label');
            label.className = 'checkbox-item';
            label.innerHTML = `
                <input type="checkbox" value="${helper.id}" class="helper-checkbox">
                <span>${helper.name}</span>
            `;
            helpersCheckbox.appendChild(label);
        });
    } catch (error) {
        console.error('Erro ao carregar ajudantes para checkbox:', error);
    }
}

// ====================================
// FUNÇÕES DE SERVIÇOS
// ====================================

/**
 * Carrega a lista de serviços da API e exibe na tela
 */
async function loadServices() {
    try {
        const services = await apiCall('/services');
        const servicesList = document.getElementById('servicesList');

        servicesList.innerHTML = '';

        if (services.length === 0) {
            servicesList.innerHTML = '<div class="empty-state"><p>Nenhum serviço cadastrado</p></div>';
            return;
        }

        services.forEach(service => {
            // Formata a data
            const serviceDate = new Date(service.service_date).toLocaleDateString('pt-BR');

            // Coleta informações dos recursos alocados
            const trucks = service.trucks?.map(t => t.plate).join(', ') || 'Nenhum';
            const drivers = service.drivers?.map(d => d.name).join(', ') || 'Nenhum';
            const helpers = service.helpers?.map(h => h.name).join(', ') || 'Nenhum';

            const card = document.createElement('div');
            card.className = 'item-card';
            card.innerHTML = `
                <div class="item-info">
                    <h4>Serviço #${service.id}</h4>
                    <p><strong>Data:</strong> ${serviceDate}</p>
                    <p><strong>Origem:</strong> ${service.origin}</p>
                    <p><strong>Destino:</strong> ${service.destination}</p>
                    <p><strong>Quantidade de Caixas:</strong> ${service.box_count}</p>
                    <p><strong>Caminhões:</strong> ${trucks}</p>
                    <p><strong>Motoristas:</strong> ${drivers}</p>
                    <p><strong>Ajudantes:</strong> ${helpers}</p>
                    ${service.notes ? `<p><strong>Observações:</strong> ${service.notes}</p>` : ''}
                </div>
                <div class="item-actions">
                    <button class="btn btn-success" onclick="editService(${service.id})">Editar</button>
                    <button class="btn btn-danger" onclick="deleteService(${service.id})">Deletar</button>
                </div>
            `;
            servicesList.appendChild(card);
        });
    } catch (error) {
        console.error('Erro ao carregar serviços:', error);
    }
}

/**
 * Carrega clientes para o select na criação de serviços
 */
async function loadClientsForSelect() {
    try {
        const clients = await apiCall('/clients');
        const clientSelect = document.getElementById('serviceClient');

        // Limpa o select (mantém a opção padrão)
        const defaultOption = clientSelect.querySelector('option[value=""]');
        clientSelect.innerHTML = '';
        clientSelect.appendChild(defaultOption);

        clients.forEach(client => {
            const option = document.createElement('option');
            option.value = client.id;
            option.textContent = client.name;
            clientSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Erro ao carregar clientes para select:', error);
    }
}

/**
 * Cria um novo serviço via formulário
 */
async function createService(event) {
    event.preventDefault();

    // Coleta os checkboxes selecionados
    const truckIds = Array.from(document.querySelectorAll('.truck-checkbox:checked'))
        .map(cb => parseInt(cb.value));

    const driverIds = Array.from(document.querySelectorAll('.driver-checkbox:checked'))
        .map(cb => parseInt(cb.value));

    const helperIds = Array.from(document.querySelectorAll('.helper-checkbox:checked'))
        .map(cb => parseInt(cb.value));

    const serviceData = {
        client_id: parseInt(document.getElementById('serviceClient').value),
        origin: document.getElementById('serviceOrigin').value,
        destination: document.getElementById('serviceDestination').value,
        box_count: parseInt(document.getElementById('serviceBoxCount').value),
        service_date: document.getElementById('serviceDate').value,
        notes: document.getElementById('serviceNotes').value || null,
        truck_ids: truckIds,
        driver_ids: driverIds,
        helper_ids: helperIds
    };

    // Validações simples
    if (!serviceData.client_id) {
        showAlert('Por favor, selecione um cliente', 'error');
        return;
    }

    try {
        await apiCall('/services', 'POST', serviceData);
        showAlert('Serviço registrado com sucesso!', 'success');
        event.target.reset();
        loadServices();
    } catch (error) {
        console.error('Erro ao criar serviço:', error);
    }
}

/**
 * Edita um serviço existente
 */
function editService(serviceId) {
    alert('Funcionalidade de edição em desenvolvimento');
}

/**
 * Deleta um serviço
 */
async function deleteService(serviceId) {
    if (!confirm('Tem certeza que deseja deletar este serviço?')) {
        return;
    }

    try {
        await apiCall(`/services/${serviceId}`, 'DELETE');
        showAlert('Serviço deletado com sucesso!', 'success');
        loadServices();
    } catch (error) {
        console.error('Erro ao deletar serviço:', error);
    }
}

// ====================================
// INICIALIZAÇÃO
// ====================================

/**
 * Carrega os dados iniciais quando a página abre
 */
window.addEventListener('DOMContentLoaded', function() {
    // Carrega os clientes inicialmente
    loadClients();
});
