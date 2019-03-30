#must return to c tutorials soon
#include <stdio.h>
/* PRINT Fahrenheit-Celsius table
  for c = 0, 5, ...., 100 */

int main()
{
  int lower, upper, step;
  float fahr, celsius;

  lower = 0; /*lower limit of temperature table*/
  upper = 100; /*upper limit */
  step = 5; /* step size*/

  celsius = lower;
  printf("Celsius  Fahrenheit \n");
  while (celsius <= upper)
    {
      fahr = ((9.0/5.0)*(celsius))+32.0;
      printf("   %4.0f   %6.1f\n", celsius, fahr);
      celsius = celsius + step;

}

}
