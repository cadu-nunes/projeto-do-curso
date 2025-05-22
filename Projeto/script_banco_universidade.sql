
-- Criação das tabelas
CREATE TABLE IF NOT EXISTS Alunos (
    MAT INTEGER PRIMARY KEY,
    nome TEXT,
    rua TEXT,
    local TEXT,
    cidade TEXT
);

CREATE TABLE IF NOT EXISTS Professores (
    COD_PROF INTEGER PRIMARY KEY,
    nome TEXT,
    rua TEXT,
    local TEXT,
    cidade TEXT
);

CREATE TABLE IF NOT EXISTS Disciplinas (
    COD_DISC INTEGER PRIMARY KEY,
    nome TEXT,
    carga_hor INTEGER
);

CREATE TABLE IF NOT EXISTS Turma (
    COD_DISC INTEGER,
    COD_TURMA INTEGER,
    COD_PROF INTEGER,
    ANO INTEGER,
    horario TEXT,
    PRIMARY KEY (COD_DISC, COD_TURMA, ANO),
    FOREIGN KEY (COD_DISC) REFERENCES Disciplinas(COD_DISC),
    FOREIGN KEY (COD_PROF) REFERENCES Professores(COD_PROF)
);

CREATE TABLE IF NOT EXISTS Historico (
    MAT INTEGER,
    COD_DISC INTEGER,
    COD_TURMA INTEGER,
    COD_PROF INTEGER,
    ANO INTEGER,
    frequencia INTEGER,
    nota REAL,
    FOREIGN KEY (MAT) REFERENCES Alunos(MAT),
    FOREIGN KEY (COD_DISC) REFERENCES Disciplinas(COD_DISC),
    FOREIGN KEY (COD_PROF) REFERENCES Professores(COD_PROF)
);

-- Inserção de dados de exemplo
INSERT INTO Alunos (MAT, nome, rua, local, cidade) VALUES
(1, 'Carlos Silva', 'Rua A', 'Centro', 'São Paulo'),
(2, 'Ana Souza', 'Rua B', 'Jardins', 'São Paulo'),
(3, 'João Lima', 'Rua C', 'Vila Mariana', 'Santos');

INSERT INTO Professores (COD_PROF, nome, rua, local, cidade) VALUES
(101, 'Prof. Ana Paula', 'Av X', 'Centro', 'São Paulo'),
(102, 'Prof. Ricardo', 'Av Y', 'Vila Nova', 'Campinas');

INSERT INTO Disciplinas (COD_DISC, nome, carga_hor) VALUES
(201, 'Matemática', 60),
(202, 'Física', 40);

INSERT INTO Turma (COD_DISC, COD_TURMA, COD_PROF, ANO, horario) VALUES
(201, 1, 101, 2025, '08:00'),
(202, 1, 102, 2025, '10:00');

INSERT INTO Historico (MAT, COD_DISC, COD_TURMA, COD_PROF, ANO, frequencia, nota) VALUES
(1, 201, 1, 101, 2025, 90, 8.5),
(2, 201, 1, 101, 2025, 85, 7.2),
(3, 202, 1, 102, 2025, 60, 5.0);
