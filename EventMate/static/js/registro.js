
function registro(){
	
	var nombres=document.getElementById('nombre_reg').value;
	var apellidos=document.getElementById('apellidos_reg').value;
	var edad=document.getElementById('edad_reg').value;
	var hobies=document.getElementById('hobies_reg').value;
	var descripcion=document.getElementById('descripcion_reg').value;
	var email=document.getElementById('email_reg').value;
	var nick=document.getElementById('nick_reg').value;
	var contraseña=document.getElementById('contraseña_reg').value;
	var pregunta=document.getElementById('combopreguntas').value;
	var respuesta=document.getElementById('respuesta_reg').value;


	alert("Nombre:"+ nombres+",Apellidos:"+ apellidos+",Edad:"+ edad+",Hobies:"+ hobies+",Descrpcion:"+ descripcion+",Email:"+ email+",Nick:"+ nick+",Contraseña:"+ contraseña+",Pregunta:"+ pregunta+",Respuesta:"+ respuesta);
	
	
	
}

/*
$(document).ready(function(){
    $("#btnregi").click(function(){
        alert("el nombre es : " + $("#nomreg").text());
        alert("usain");
    });
});
*/
