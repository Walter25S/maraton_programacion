import React, { useState } from 'react';
import styles from '../styles/TeamCard.css';



export function TeamCard() {
  const [nombreEquipo, setNombreEquipo] = useState('');
  const [descripcionEquipo, setDescripcionEquipo] = useState('');
  const [integrantes, setIntegrantes] = useState([]);
  const [descripcionIntegrantes, setDescripcionIntegrantes] = useState([]);

  const agregarIntegrante = () => {
    setIntegrantes([...integrantes, '']);
    setDescripcionIntegrantes([...descripcionIntegrantes, '']);
  };

  const eliminarIntegrante = (index) => {
    const updatedIntegrantes = [...integrantes];
    updatedIntegrantes.splice(index, 1);
    setIntegrantes(updatedIntegrantes);

    const updatedDescripcionIntegrantes = [...descripcionIntegrantes];
    updatedDescripcionIntegrantes.splice(index, 1);
    setDescripcionIntegrantes(updatedDescripcionIntegrantes);
  };

  const handleNombreEquipoChange = (event) => {
    setNombreEquipo(event.target.value);
  };

  const handleDescripcionEquipoChange = (event) => {
    setDescripcionEquipo(event.target.value);
  };

  const handleIntegranteChange = (event, index) => {
    const updatedIntegrantes = [...integrantes];
    updatedIntegrantes[index] = event.target.value;
    setIntegrantes(updatedIntegrantes);
  };

  const handleDescripcionIntegranteChange = (event, index) => {
    const updatedDescripcionIntegrantes = [...descripcionIntegrantes];
    updatedDescripcionIntegrantes[index] = event.target.value;
    setDescripcionIntegrantes(updatedDescripcionIntegrantes);
  };

  return (
    <div>
      <head>
        <title>Maratón de Programación 2023</title>
      </head>
      <h1>Maratón de Programación 2023</h1>
      <form action="procesar.php" method="post">
        <label htmlFor="nombre_equipo">Nombre del Equipo:</label>
        <input
          type="text"
          id="nombre_equipo"
          name="nombre_equipo"
          placeholder="Nombre del equipo"
          value={nombreEquipo}
          onChange={handleNombreEquipoChange}
          required
        />
        <br />
        <label htmlFor="descripcion_equipo">Descripción del Equipo:</label>
        <textarea
          id="descripcion_equipo"
          name="descripcion_equipo"
          placeholder="Descripción del equipo"
          value={descripcionEquipo}
          onChange={handleDescripcionEquipoChange}
        />
        <br />
        <h2>Añadir Integrantes</h2>
        <div id="integrantes">
          {integrantes.map((integrante, index) => (
            <div key={index}>
              <input
                type="text"
                name="integrante[]"
                placeholder="Nombre del Integrante"
                value={integrante}
                onChange={(event) => handleIntegranteChange(event, index)}
              />
              <textarea
                name="descripcion_integrante[]"
                placeholder="Descripción del Integrante"
                value={descripcionIntegrantes[index]}
                onChange={(event) => handleDescripcionIntegranteChange(event, index)}
              />
              <button type="button" onClick={() => eliminarIntegrante(index)}>
                Eliminar Integrante
              </button>
            </div>
          ))}
        </div>
        <button type="button" id="agregar_integrante" onClick={agregarIntegrante}>
          Añadir Integrante
        </button>
        <br />
        <input type="submit" value="Enviar" />
      </form>
    </div>
  );
}





  