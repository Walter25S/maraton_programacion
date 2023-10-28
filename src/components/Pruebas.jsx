export const TeamCard = () => {
    

    return (
        <div>
            <section>
                <h1>Maraton de programación 2023-2</h1>
                <form>
                    <span>
                        <h1>Crear equipo</h1>
                        <label htmlFor="Nombre del equipo">Nombre del equipo: </label>
                        <input type="text" id="nombre_equipo" name="nombre_equipo" placeholder="Nombre del equipo" required></input>
                    </span>

                    <span>
                        <label htmlFor="Descripción del equipo">Descripción del equipo: </label>
                        <input type="text" id="Descripción_equipo" name="Descripción_equipo" placeholder="Descripción del equipo" required></input>
                    </span>
                    <br />
                    <h1>Integrantes</h1>

                    <span>
                        <label htmlFor="Nombre del Integrante">Nombre del Integrante: </label>
                        <input type="text" id="Nombre_Integrante" name="Nombre_Integrante" placeholder="Nombre del Integrante" required></input>
                    </span>
                    <br />
                    <span>
                        <label htmlFor="Descripción del integrante">Descripción del integrante: </label>
                        <textarea name="Descripción_integrante" id="Descripción_integrante" cols="30" rows="5"></textarea>

                    </span>

                    <span>
                        <button type='button' id="añadir_integrante">
                            Adicionar integrante
                        </button>
                    </span>

                    <span>
                        <button type='button' id="eliminar_integrante">
                            Eliminar integrante
                        </button>
                    </span>
                    <br />
                    <input type="submit" value="Enviar"></input>

                </form>
            </section>
        </div>
    )
}