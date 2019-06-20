/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

The primitive data types of Javascript are:

String, Numbers, Bigint,  Boolean, null, undefined, (and Symbols).

These are

18:44

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */

const name = 'James';     // <——— String

const age0 = 30;          // <——— Number
const age1 = 30.5;        // <——— Number
const age2 = 30.523423;   // <——— Number

const isOld = false;      // <——— Boolean
const isYoung = true;     // <——— Boolean

const x = null;           // <——— null

const y = undefined;      // <——— undefined
let z;                    // <——— undefined


/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */
/* How to check type ? */

console.log(typeof name)           // Output: string

console.log(typeof age0)           // Output: number
console.log(typeof age1)           // Output: number
console.log(typeof age2)           // Output: number

console.log(typeof isOld)          // Output: boolean
console.log(typeof isYoung)        // Output: boolean

console.log(typeof x)              // Output: object
/* Says 'object' but
that's just a bogus
result, its actually
'null' */

console.log(typeof y)              // Output: undefined
console.log(typeof z)              // Output: undefined

/* — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — */
