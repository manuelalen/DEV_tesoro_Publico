<?php
// Obtener los valores del formulario
$cantidad = $_POST["cantidad"];
$concepto = $_POST["concepto"];



// Conectarse a la base de datos
$servername = "localhost";
$username = "tesoro";
$password = "tesoro2023";
$dbname = "Tesoro";
$conn = new mysqli($servername, $username, $password, $dbname);
echo "Cantidad: " . $cantidad . "<br>";
echo "Concepto: " . $concepto . "<br>";

// Comprobar si se ha producido un error al conectarse a la base de datos
if ($conn->connect_error) {
    die("Error al conectar a la base de datos: " . $conn->connect_error);
}

// Ejecutar la consulta para insertar los datos en la tabla
$sql = "INSERT INTO Tesoro.BancoCentral (cantidad, concepto) VALUES ('$cantidad', '$concepto')";
echo $sql;

if ($conn->query($sql) === TRUE) {
    echo "Datos insertados correctamente en la base de datos";
} else {
    echo "Error al insertar los datos en la base de datos: " . mysqli_error($conn);
}

// Cerrar la conexión a la base de datos
$conn->close();
?>
