// Calcolo dell'età
var birthYear = prompt("Inserisci l'anno di nascita:");
var currentYear = new Date().getFullYear();
var age = currentYear - birthYear;
alert("La tua età è: " + age);
