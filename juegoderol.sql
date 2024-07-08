-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 08-07-2024 a las 23:25:24
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `juegoderol`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipamiento`
--

CREATE TABLE `equipamiento` (
  `id_equip` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `equipamiento`
--

INSERT INTO `equipamiento` (`id_equip`, `nombre`, `descripcion`) VALUES
(1, 'Espada de Acero', 'Espada bien equilibrada'),
(2, 'Escudo de Roble', 'Escudo robusto de madera de ro'),
(3, 'Armadura de Cuero', 'Armadura ligera de cuero'),
(4, 'Varita Mágica', 'Varita que amplifica el poder'),
(5, 'Botas de Velocidad', 'Botas que aumentan velocidad'),
(6, 'Capa de inivisibilid', 'Capa que otorga invisibilidad'),
(7, 'Casco de Hierro', 'Casco resistente de hierro'),
(8, 'Anillo de Regeneraci', 'Anillo que acelera la curación');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `descripcion` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id_estado`, `nombre`, `descripcion`) VALUES
(1, 'Vivo', 'El personaje esta vivo'),
(2, 'Muerto', 'El personaje esta Muerto'),
(3, 'Congelado', 'El personaje esta Congelado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `gamemaster`
--

CREATE TABLE `gamemaster` (
  `id_gm` int(11) NOT NULL,
  `gm_personaje_id` int(11) DEFAULT NULL,
  `gm_usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `habilidad`
--

CREATE TABLE `habilidad` (
  `id_habilidad` int(11) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `hab_raza_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `habilidad`
--

INSERT INTO `habilidad` (`id_habilidad`, `nombre`, `descripcion`, `hab_raza_id`) VALUES
(1, 'Golpe Poderoso', 'Ataque devastador con daño extra.', 1),
(2, 'Escudo Defensivo', 'Aumenta defensa temporalmente.', 1),
(3, 'Corte Veloz', 'Ataques rápidos con daño múltiple.', 1),
(4, 'Grito de Guerra', 'Aumenta moral y ataque de aliados.', 1),
(5, 'Carga Imparable', 'Carga con fuerza arrolladora.', 1),
(6, 'Recuperación Rápida', 'Cura pequeña cantidad de salud.', 1),
(7, 'Parada Maestra', 'Incrementa bloqueo de ataques.', 1),
(8, 'Golpe Desarmador', 'Desarma al enemigo temporalmente.', 1),
(9, 'Bola de Fuego', 'Lanza bola de fuego con daño en área.', 2),
(10, 'Escudo Mágico', 'Absorbe una cantidad de daño.', 2),
(11, 'Teletransportación', 'Teletransporta a corta distancia.', 2),
(12, 'Rayo de Hielo', 'Dispara rayo de hielo que reduce velocid', 2),
(13, 'Curación Rápida', 'Restaura salud moderada.', 2),
(14, 'Explosión Arcana', 'Explosión de energía que daña enemigos c', 2),
(15, 'Invisibilidad', 'Vuelve invisible temporalmente.', 2),
(16, 'Invocación de Elemental', 'Invoca elemental para luchar.', 2),
(17, 'Golpe Aplastante', 'Ataque poderoso con alta probabilidad de', 3),
(18, 'Muro de Carne', 'Aumenta resistencia física temporalmente', 3),
(19, 'Carga Brutal', 'Carga hacia adelante derribando enemigos', 3),
(20, 'Rugido Intimidante', 'Asusta enemigos cercanos, reduciendo mor', 3),
(21, 'Regeneración Vigorosa', 'Restaura significativa salud brevemente.', 3),
(22, 'Golpe de Tierra', 'Ondas de choque que dañan y derriban.', 3),
(23, 'Agarre Brutal', 'Agarra y lanza a un enemigo.', 3),
(24, 'Fuerza Descomunal', 'Aumenta temporalmente daño y velocidad.', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jugador`
--

CREATE TABLE `jugador` (
  `id_jugador` int(11) NOT NULL,
  `jg_usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personaje`
--

CREATE TABLE `personaje` (
  `id_personaje` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `nivel` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL,
  `poder_id` int(11) DEFAULT NULL,
  `raza_id` int(11) DEFAULT NULL,
  `habilidad_id` int(11) DEFAULT NULL,
  `equip_id` int(11) DEFAULT NULL,
  `habilidad_id1` int(11) DEFAULT NULL,
  `habilidad_id2` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `poder`
--

CREATE TABLE `poder` (
  `id_poder` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `descripcion` varchar(40) DEFAULT NULL,
  `poder_raza_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `poder`
--

INSERT INTO `poder` (`id_poder`, `nombre`, `descripcion`, `poder_raza_id`) VALUES
(1, 'Golpe Colosal', 'Ataque poderoso', 1),
(2, 'Defensa Imparable', 'Incrementa defensa temporalmente', 1),
(3, 'Furia Berserker', 'Aumenta velocidad y fuerza', 1),
(4, 'Muro de Escudos', 'Crea una barrera protectora', 1),
(5, 'Curación Mayor', 'Restaura mucha salud', 2),
(6, 'Invisibilidad', 'Vuelve al mago invisible brevemente', 2),
(7, 'Tormenta de Rayos', 'Invoca una tormenta que daña a todos los', 2),
(8, 'Control Mental', 'Controla a un enemigo por poco tiempo', 2),
(9, 'Mazo Destructor', 'Golpea con un mazo causando daño masivo.', 3),
(10, 'Furia Incontenible', 'Aumenta temporalmente la fuerza y veloci', 3),
(11, 'Garras Afiladas', 'Ataca con garras causando sangrado prolo', 3),
(12, 'Torbellino de Golpes', 'Realiza una serie de golpes rápidos a lo', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `raza`
--

CREATE TABLE `raza` (
  `id_raza` int(11) NOT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `raza`
--

INSERT INTO `raza` (`id_raza`, `nombre`, `tipo`) VALUES
(1, 'Humano', 'Guerrero'),
(2, 'Elfo', 'Mago'),
(3, 'Ogro', 'Luchador');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `contrasena` varchar(100) NOT NULL,
  `area` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipamiento`
--
ALTER TABLE `equipamiento`
  ADD PRIMARY KEY (`id_equip`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `gamemaster`
--
ALTER TABLE `gamemaster`
  ADD PRIMARY KEY (`id_gm`),
  ADD KEY `gm_usuario_id` (`gm_usuario_id`),
  ADD KEY `gm_personaje_id` (`gm_personaje_id`);

--
-- Indices de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD PRIMARY KEY (`id_habilidad`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `hab_raza_id` (`hab_raza_id`);

--
-- Indices de la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD PRIMARY KEY (`id_jugador`),
  ADD KEY `jg_usuario_id` (`jg_usuario_id`);

--
-- Indices de la tabla `personaje`
--
ALTER TABLE `personaje`
  ADD PRIMARY KEY (`id_personaje`),
  ADD KEY `estado_id` (`estado_id`),
  ADD KEY `poder_id` (`poder_id`),
  ADD KEY `raza_id` (`raza_id`),
  ADD KEY `habilidad_id` (`habilidad_id`),
  ADD KEY `equip_id` (`equip_id`),
  ADD KEY `personaje_ibfk_2` (`usuario_id`),
  ADD KEY `fk_personaje_habilidad1` (`habilidad_id1`),
  ADD KEY `fk_personaje_habilidad2` (`habilidad_id2`);

--
-- Indices de la tabla `poder`
--
ALTER TABLE `poder`
  ADD PRIMARY KEY (`id_poder`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `poder_raza_id` (`poder_raza_id`);

--
-- Indices de la tabla `raza`
--
ALTER TABLE `raza`
  ADD PRIMARY KEY (`id_raza`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `contraseña` (`contrasena`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipamiento`
--
ALTER TABLE `equipamiento`
  MODIFY `id_equip` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `gamemaster`
--
ALTER TABLE `gamemaster`
  MODIFY `id_gm` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `habilidad`
--
ALTER TABLE `habilidad`
  MODIFY `id_habilidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `jugador`
--
ALTER TABLE `jugador`
  MODIFY `id_jugador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `personaje`
--
ALTER TABLE `personaje`
  MODIFY `id_personaje` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;

--
-- AUTO_INCREMENT de la tabla `poder`
--
ALTER TABLE `poder`
  MODIFY `id_poder` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `raza`
--
ALTER TABLE `raza`
  MODIFY `id_raza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=56;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `gamemaster`
--
ALTER TABLE `gamemaster`
  ADD CONSTRAINT `gamemaster_ibfk_1` FOREIGN KEY (`gm_usuario_id`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `gamemaster_ibfk_2` FOREIGN KEY (`gm_personaje_id`) REFERENCES `personaje` (`id_personaje`);

--
-- Filtros para la tabla `habilidad`
--
ALTER TABLE `habilidad`
  ADD CONSTRAINT `habilidad_ibfk_1` FOREIGN KEY (`hab_raza_id`) REFERENCES `raza` (`id_raza`);

--
-- Filtros para la tabla `jugador`
--
ALTER TABLE `jugador`
  ADD CONSTRAINT `jugador_ibfk_1` FOREIGN KEY (`jg_usuario_id`) REFERENCES `usuario` (`id`);

--
-- Filtros para la tabla `personaje`
--
ALTER TABLE `personaje`
  ADD CONSTRAINT `fk_personaje_habilidad1` FOREIGN KEY (`habilidad_id1`) REFERENCES `habilidad` (`id_habilidad`),
  ADD CONSTRAINT `fk_personaje_habilidad2` FOREIGN KEY (`habilidad_id2`) REFERENCES `habilidad` (`id_habilidad`),
  ADD CONSTRAINT `personaje_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `estado` (`id_estado`),
  ADD CONSTRAINT `personaje_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `personaje_ibfk_3` FOREIGN KEY (`poder_id`) REFERENCES `poder` (`id_poder`),
  ADD CONSTRAINT `personaje_ibfk_4` FOREIGN KEY (`raza_id`) REFERENCES `raza` (`id_raza`),
  ADD CONSTRAINT `personaje_ibfk_5` FOREIGN KEY (`habilidad_id`) REFERENCES `habilidad` (`id_habilidad`),
  ADD CONSTRAINT `personaje_ibfk_6` FOREIGN KEY (`equip_id`) REFERENCES `equipamiento` (`id_equip`);

--
-- Filtros para la tabla `poder`
--
ALTER TABLE `poder`
  ADD CONSTRAINT `poder_ibfk_1` FOREIGN KEY (`poder_raza_id`) REFERENCES `raza` (`id_raza`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
