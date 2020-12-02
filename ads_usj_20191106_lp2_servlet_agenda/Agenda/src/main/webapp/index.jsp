<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@page import="entity.Agenda" %>
<%@page import="entity.Contato" %>
<%@page import="java.util.ArrayList" %>
<%@page import="java.util.List" %>

<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<title>Agenda</title>
	<style>
		.contatos {
			width: 30%;
			margin: 10px auto;
			padding: 10px;
			border: 1px solid;
		}
		.contatos:hover {
			width: 30%;
			margin: 10px auto;
			padding: 10px;
			border: 1px dashed;
		}
		h1.contatos{
			border: none;
		}
		h1.contatos:hover{
			border: none;
		}
	</style>
	<% Agenda agenda = new Agenda(); 
	agenda.toAgenda("Jorder","00-00000"); 
	agenda.toAgenda("Osmar","00-00000"); 
	agenda.toAgenda("Pdero","00-00000"); 
	agenda.toAgenda("Fernando","00-00000"); 
	agenda.toAgenda("Micael","00-00000"); 
	%>
</head>

<body>
	<div class="agenda">
		<section>
			<div>
				<h1 class="contatos">Contatos</h1>
				<%
					for (Contato contato : agenda.getContatos()){
					%> <div class="contatos">
					<p> Nome: <span><% out.println(""+contato.getNome()); %> </span> </p>
					<p> Telefone: <span><% out.println(""+contato.getTelefone()); %> </span> </p>
				</div>
				<% }
					%>
			</div>
		</section>
	</div>
</body>

</html>