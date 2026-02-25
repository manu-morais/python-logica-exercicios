import math
an = int(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O seno do ângulo é {sen:.2f}, o cosceno é {cos:.2f} e a tangente é {tan:.2f}')