# `007` Hours and minutes

En este ejercicio vamos a suponer que es medianoche, queremos que con la funci贸n `hours_minutes` que hemos previsto para t铆, nos digas cu谩nto tiempo ha pasado desde entonces con los segundos que se introduzcan como par谩metro.

## 馃摑 Instrucciones:

1. Completa la funci贸n para que retorne el resultado esperado.

2. Realiza dos calculos con los segundos que se pasan por par谩metro en la funci贸n para que uno calcule la hora seg煤n los segundos que han pasado y el otro para saber los minutos `(hora , minutos)`

## Ejemplo 1:

```py
output = hours_minutes(3900)
print(output) # (1, 5)
```

## Ejemplo 2:

```py
output = hours_minutes(60)
print(output) # (0, 1)
```

## 馃挕 Pistas:

+ Recuerda cuantos segundos hay en una hora (3600) y cuantos segundos en un minuto (60).

+ Si no sabes c贸mo empezar la soluci贸n a esta asignaci贸n, por favor, revisa la teor铆a en esta lecci贸n: https://snakify.org/lessons/print_input_numbers/

+ Tambi茅n puedes intentar paso a paso con trozos de la teor铆a: https://snakify.org/lessons/print_input_numbers/steps/1/

[comment]: <Solution: (secs//3600, secs//60)>