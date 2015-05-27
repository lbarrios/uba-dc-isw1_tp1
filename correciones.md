# TODO sobre Actividades
1. ~~poner las discusiones o-refs en seccion discusion~~
2. ~~refinar 1.1.1.2.1.4.2.4 como el concepto de permitir rehacer el pedido con subobjetivos ofrecer rehacer el pedido(con un mail, el agente correo) y mantener un link que apunte a la orden de compra previa.~~
3. en registro online poner, como subobjetivo de verificar datos(1.1.1.1.1.1.2), "verificar calidad de contrasenia" (la parte de ingresarla quizas pueda estar incluida en "ingresar datos de identificacion")
4. en registro de sucursal hace falta hablar de hacerle llegar la contrasenia auto-generada (y obligarlo a cambiarla cuando se loguea). hay que decidir si se la mandamos por mail(facil y barato) o por correo(validas domicilio de forma robusta) **(y si se la entregas en mano?)**
5. en las dos ramas de registro, hace falta verificar la cuenta con un mail. para no replicar en las ramas, podes poner en presencial "verificar mail", y en online "mandar mail de bienvenida"
6. mandar mail de verificacion de compra
7. Logística debería quitar de stock los productos que ya están vencidos

# preguntas a tutores
1.  Hace falta refinar "mostrar recomendaciones(1.1.1.1.2.2)" como evaluar historial, 
    evaluar perfil del cliente, etc.. , o se puede explicar nomas en el texto?

# LISTO
# Contexto
7. Revisar que los eventos sean interacciones entre dos agentes, y no eventos internos del sistema. Como "Evalua ingreso por red social", "Contabiliza ingresos por compras", "Añade no-recepcion al perfil", "Cliente se traslada a sucursal"
8. Sobre el fenomeno 8.E, el tutor marcó: "El sistema electrónico generalmente no provee la posibilidad de rehacer el pedido al cliente. El encargado de esto es el Sistema." 
	Ahora: El sistema envia la propuesta de rehacer el pedido y el link al pedido no entregado al Sistema de Correo. y El Sistema de Correo envia mail al Cliente. 
9. Los eventos 11.A y 11.B no aparecen en el diagrama de contexto. 
10. La sucursal podria ahorrarse todo el trabajo de validar los datos del cliente en el registro presencial si hace la carga online del usuario, y que el sistema haga la validacion como si fuera un caso de registro online normal. ~~ Es un o-refinamiento. Dos formas que no se intersecan. 
