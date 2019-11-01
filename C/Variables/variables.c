
/* Variable Types, Storage Classes, Sizes in C */

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	char 		var;
	int 		var;
	float 		var;
	double 		var;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	unsigned 	var;
	signed 		var;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	short 		var;
	long 		var;
	long long 	var;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	const 		int a;
	restrict 	int a;
	volatile	int a;
	_Atomic 	int a;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	auto 		int a;
	register 	int a;
	static 		int a;
	extern 		int a;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	char 		*var;
	int 		*var;
	float 		*var;
	double 		*var;
	void 		*var;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a;

	a = 19;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a = 19;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a = 19, b = 20, c = 21, d = 22;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a = 19,
		b = 20,
		c = 21,
		d = 22;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a, b, c, d;

	a = 19;
	b = 20;
	c = 21;
	d = 22;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	int a;
	int b;
	int c;

	a = b = c = 100;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	a = 200;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	void say(char *str)
	{
		printf("%s", str);
	}

	char msg[] = "Hello, world!\n";
	say(msg);

	say("Hello, world!\n");

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

	volatile struct employee
	{
	    char *name;
	    int   birthdate; 	/* name, birthdate, job_code, and salary are */
	    int   job_code;  	/* treated as though declared with volatile. */
	    float salary;
	} a, b;          		/*  All members of a and b are volatile-qualified  */

	struct employee2
	{
	    char *name;
	    volatile int birthdate;  /*  Only this member is qualified    */
	    int job_code;
	    float salary;
	} c, d;

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */








/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */




