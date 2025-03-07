/*ATIVIDADE */
CREATE DATABASE atividade;

USE atividade;

CREATE TABLE TabelaCliente (
	id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100) NOT NULL,
    cnh_cliente VARCHAR(11) NOT NULL,
	telefone_cliente VARCHAR(15) NOT NULL
);
CREATE TABLE TabelaVeiculo (
	id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    modelo_veiculo VARCHAR(100) NOT NULL,
    ano_veiculo YEAR NOT NULL,
	placa_veiculo  VARCHAR(10) NOT NULL,
    disponibilidade ENUM('disponivel','alugado')
);
CREATE TABLE TabelaFuncionario (
	id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome_funcionario VARCHAR(100) NOT NULL,
    cargo_funcionario VARCHAR(100) NOT NULL,
	telefone_funcionario  VARCHAR(15) NOT NULL
);
CREATE TABLE TabelaAluguel (
	id_aluguel INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    	FOREIGN KEY(id_cliente) REFERENCES TabelaCliente(id_cliente),
    id_veiculo INT,
    	FOREIGN KEY(id_veiculo) REFERENCES TabelaVeiculo(id_veiculo),
    id_funcionario INT,
    	FOREIGN KEY(id_funcionario) REFERENCES TabelaFuncionario(id_funcionario),
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL
);

INSERT INTO TabelaCliente (nome_cliente, cnh_cliente, telefone_cliente) 
VALUES
('João Silva', '12345678901', '11987654321'),
('Maria Oliveira', '98765432102', '11976543210'),
('Carlos Souza', '45612378903', '11965432109');

INSERT INTO TabelaVeiculo (modelo_veiculo, ano_veiculo, placa_veiculo, disponibilidade) 
VALUES
('Ford Ka', 2020, 'ABC-1234', 'disponivel'),
('Chevrolet Onix', 2019, 'DEF-5678', 'disponivel'),
('Fiat Uno', 2018, 'GHI-9101', 'alugado');

INSERT INTO TabelaFuncionario (nome_funcionario, cargo_funcionario, telefone_funcionario) 
VALUES
('Ana Souza', 'Atendente', '11988887777'),
('Ricardo Lima', 'Gerente', '11999996666'),
('Fernanda Costa', 'Supervisor', '11977778888');

INSERT INTO TabelaAluguel (id_cliente, id_veiculo, id_funcionario, data_inicio, data_fim) 
VALUES
(1, 3, 2, '2025-03-01', '2025-03-10'), 
(2, 1, 1, '2025-03-05', '2025-03-15'), 
(3, 2, 3, '2025-03-07', '2025-03-17'); 

/* Consultas SQL */
-- 1 Crie uma consulta para listar todos os contratos de aluguel, mostrando os nomes dos clientes,
-- os modelos dos veículos e os nomes dos funcionários responsáveis.

SELECT 
    TabelaCliente.nome_cliente, 
    TabelaVeiculo.modelo_veiculo, 
    TabelaFuncionario.nome_funcionario
FROM TabelaAluguel
JOIN TabelaCliente ON TabelaAluguel.id_cliente = TabelaCliente.id_cliente
JOIN TabelaVeiculo ON TabelaAluguel.id_veiculo = TabelaVeiculo.id_veiculo
JOIN TabelaFuncionario ON TabelaAluguel.id_funcionario = TabelaFuncionario.id_funcionario;

-- 2
SELECT 
    MONTH(data_inicio) AS mes, 
    YEAR(data_inicio) AS ano, 
    COUNT(id_veiculo) AS total_veiculos_alugados
FROM TabelaAluguel
GROUP BY YEAR(data_inicio), MONTH(data_inicio)
ORDER BY ano, mes;

-- 3
SELECT * 
FROM TabelaVeiculo 
WHERE disponibilidade = 'disponivel';

-- 4
UPDATE TabelaVeiculo 
SET disponibilidade = 'alugado'  -- Ou 'disponivel'
WHERE id_veiculo = <ID_DO_VEICULO>;
