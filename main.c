/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mloureir <mloureir@42porto.com>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/08/28 14:40:21 by mloureir          #+#    #+#             */
/*   Updated: 2025/09/01 11:45:54 by mloureir         ###   ########.pt       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_READ 500

char	*ft_strjoin(char *tojoin, char *tocpy)
{
	char	*newstr;

	newstr = malloc(strlen(tojoin) + strlen(tocpy) + 1);
	int	i = 0;
	while (tojoin[i] != '\0')
	{
		newstr[i] = tojoin[i];
		i++;
	}
	int	j = 0;
	while (tocpy[j] != '\0')
	{
		newstr[i] = tocpy[j];
		i++;
		j++;
	}
	newstr[i] = '\0';
	free(tojoin);
	return (newstr);
}

char	*read_for_buffer(FILE *csv)
{
	char	*helper;
	char	*toret;
	int		started = 0;

	helper = calloc(sizeof(char), 2);
	toret = malloc(1);
	toret[0] = '\0';
	while ((*helper != '\n' && *helper != '\0') || (started == 0))
	{
		started = 1;
		fgets(helper, 2, csv);
		if (helper == NULL)
			return (strdup(""));
		toret = ft_strjoin(toret, helper);
	}
	free(helper);
	return (toret);
}

 int	get_f_size()
{
	FILE *read_size = fopen("users.csv", "r");
	int	toret = 0;
	char	temp[MAX_READ];

	while (fgets(temp, MAX_READ, read_size))
		toret += 1;
	fclose(read_size);
	return (toret);
}

void	treatline(char *buffer)
{
	FILE *towrite = fopen("output.csv", "a+");
	int		i = 0;
	int		j = 0;
	while (buffer[i] != ';')
		i++;
	buffer += i + 1;
	i = 0;
	while (buffer[i] != ';')
	{
		j++;
		i++;
	}
	buffer[i] = '\n';
	buffer[i + 1] = '\0';
	fprintf(towrite, "%s", buffer);
	fclose(towrite);
}

int main()
{
	FILE *csv = fopen("users.csv", "r");
	if (!csv)
	{
		perror("\033[0;31mThe input file doesn't exist\033[0m\n");
		return (-1);
	}

	int	file_size = get_f_size();

	int	i = 0;
	char	*buffer;
	

	while (i < file_size)
	{
		buffer = read_for_buffer(csv);
		if (i != 0)
			treatline(buffer);
		else
		{
			FILE *towrite = fopen("output.csv", "w");
			fclose(towrite);
		}
		free(buffer);
		i++;
	}
	fclose(csv);
	return (0);
}
