<%@page import="java.sql.Connection"%>
<%@page import="java.sql.DriverManager"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Cadastro de produtos</title>
    </head>
    <body>
        <%
        //receber dados digitados no formulario cadpro.html
        int codigo;
        String noms,marca;
        double preco;
        codigo=Interger.parseInt(request.getParameter("codigo"));
        nome=request.getParameter("nome");
        marca=request.getParameter("marca");
        preco=Double.parsetDouble(request.getParameter("preco"));
%>
    </body>
</html>
