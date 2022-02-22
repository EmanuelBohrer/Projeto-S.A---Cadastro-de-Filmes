-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 14-Dez-2021 às 21:23
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projetosa`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `db_user`
--

CREATE TABLE `db_user` (
  `id` int(11) NOT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL,
  `permissao` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `db_user`
--

INSERT INTO `db_user` (`id`, `nome`, `senha`, `permissao`) VALUES
(1, 'admin', '182', 'master'),
(2, 'klaus', '123', 'user');

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes`
--

CREATE TABLE `filmes` (
  `id_filme` int(11) NOT NULL,
  `titulo` varchar(30) NOT NULL,
  `genero` varchar(15) NOT NULL,
  `ano` varchar(4) DEFAULT NULL,
  `diretor` varchar(20) NOT NULL,
  `nota` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `filmes`
--

INSERT INTO `filmes` (`id_filme`, `titulo`, `genero`, `ano`, `diretor`, `nota`) VALUES
(1, 'O Farol', 'Drama', '2019', 'Jon Eggers', 7.5),
(2, 'Logan', 'Drama', '2017', 'James Mangold', 8.1),
(3, 'Carros', 'Animação', '2006', 'Joe Ranft', 7.1),
(4, 'Corra', 'Terror', '2017', 'Jordan Peele', 7.7),
(5, 'Django', 'Ação', '2012', 'Quentin Tarantino', 8.5),
(6, 'Pulp Fiction', 'Ação', '1994', 'Quentin Tarantino', 8.9),
(8, 'Pantera Negra', 'Ação', '2018', 'Ryan Coogler', 7.3),
(9, 'O Espetacular Homem Aranha', 'Ação', '2012', 'Marc Webb', 6.9),
(10, 'Drive', 'Ação', '2012', 'Nicolas Winding', 4.2),
(12, 'A casa Monstro', 'Animação', '2005', 'Gil Kenan', 4.5),
(13, 'Coraline e o Mundo Sombrio', 'Animação', '2009', 'Henry Selick', 4.8);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `db_user`
--
ALTER TABLE `db_user`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `filmes`
--
ALTER TABLE `filmes`
  ADD PRIMARY KEY (`id_filme`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `db_user`
--
ALTER TABLE `db_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
