#include <stdio.h>
#include <strings.h>

int	isUnique(char *str)
{
	char arr[256];

	bzero(arr,256);
	while (*str)
	{
		if (arr[*str] == '\0')
			arr[*str] = *str;
		else if (arr[*str] == *str)
			return (-1);
		str++;
	}
	return (1);
}

int main(void)
{
	char *str = "abadefghi";

	if (isUnique(str))
		printf("yes\n");
	else
		printf("No");

}
