package grafosgenericos.grafos;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;

public class Grafo<T> {
    /** Este atributo nos permitirá definir el tipo de grafo a crear
     *  true = Grafo Dirigido,
     *  false = Grafo NO Dirigido.
     */
    
    private boolean dirigido;
    /** Se crea una Lista <LLave, Valor> para almacenar los vértices del grafo
     *  Primer parámetro es la llave en este caso el Vértice del grafo,
     *  Segundo parámetro es la lista de Aristas o conexiones con otros Vértices.
     */
    
    private HashMap<T, List<Arista<T>>> vertices;
    
    /**
     * Constructor sobrecargado para crear un nuevo objeto Grafo
     * @param dirigido [true | false] determina si el grafo es dirigido o 
     * NO dirigido.
     */
    public Grafo(boolean dirigido){
        this.vertices = new HashMap<>();
        this.dirigido = dirigido;
