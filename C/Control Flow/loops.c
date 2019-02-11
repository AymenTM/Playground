
/* Loops in C */

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */


	while ( expression ) { statement }


	while (condition)
	{
		// do this
	}


	int i = 0;			// incrementor
	while (i < n)		// condition
	{
		// do this
		i++;			// increment incrementor
	}


	int i = -1;
	while (++i < n)		// we increment, then check the condition
	{
		// do this
	}


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */


	for ( init_clause ; expression ; iteration_expression ) { statement }


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */


	for (initialise vars; condition ; action_on_iteration)
	{
		// do this
	}


	for (int i = 0; i < n; i++)
	{
		// do this
	}


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */


	do { statement } while ( expression )


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */


	do
	{
		// do this
	}
	while (condition);


	int i = 0;
	do
	{
		// do this
		i++;
	}
	while (i < n)


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */
