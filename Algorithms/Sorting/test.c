#include <stdio.h>

int main(){ 
	int i[] = {0,1,2};
	int count = 0;
	printf("%i-%i\n", i[count++], count );
	printf("%i-%i\n", i[count++], count );
	printf("%i-%i\n", i[count++], count );
}