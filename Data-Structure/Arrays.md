# Data Structures

- Data structures manage how data is stored and accessed.
- Data Structures in TypeScript are ways to store, organize, and manage data efficiently so that it can be accessed, modified, and processed easily.
- Data Structures decide how data is arranged in memory and how we work with it.
- Data structures are building blocks or raw material for any software program.
- One can't become a good programmer without a sound understanding of data structures.
- Big O notation is used to measure how the running time or space requirements of a program grow as the input size grows.

---

### Arrays
- An array is a linear data structure used to store multiple values in a single variable. In TypeScript, arrays can store numbers, strings, objects, or other types.
```ts
// Creating an Array
// Array<number> == number[]

let numbers: number[] = [10, 20, 30, 40, 50];

let fruits: string[] = ["Apple", "Banana", "Orange"];

let scores: Array<number> = [85, 90, 95];

console.log(numbers);
console.log(fruits);
console.log(scores);

// Accessing and Updating Elements
let numbers: number[] = [10, 20, 30, 40];

numbers[1] = 25;

console.log(numbers[1]);
console.log(numbers);
console.log(numbers.length);

// push() — Add an element to the end
let arr = [1, 2, 3];
arr.push(4);
console.log(arr);

// pop() — Remove the last element
let arr = [1, 2, 3];
arr.pop();
console.log(arr);

// indexOf() — Find an element's index
let arr = [1, 2, 3];
console.log(arr.indexOf(2));

// filter() — Select matching elements
let arr = [1, 2, 3, 4, 5];
let results = arr.filter(n => n > 3);
console.log(results);

// map() — Transform every element
let arr = [1, 2, 3];
let result = arr.map(n => n * 2);
console.log(result);


// Loop Through an Array
const fruits: string[] = ["Apple", "Banana", "Orange"];

// Using a for loop
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

// Using for...of
for (const fruit of fruits) {
    console.log(fruit);
}

// Using forEach
fruits.forEach((fruit) => {
    console.log(fruit);
})


// Array Data Structure: Searching and Inserting
class ArrayOperations {
    private data: number[] = [];

    // Insert at the end
    insert(value: number): void {
        this.data.push(value);
    }

    // Search for a value
    search(value: number): number {
        return this.data.indexOf(value);
    }

    // Delete the first matching value
    delete(value: number): boolean {
        const index = this.data.indexOf(value);

        if (index == -1) {
            return false;
        }

        this.data.splice(index, 1);
        return true;
    }

    // Display all elements
    display(): number[] {
        return [...this.data];
    }
}

const arr = new ArrayOperations();
arr.insert(10);
arr.insert(20);
arr.insert(30);

console.log(arr.display());
console.log(arr.search(20));

arr.delete(20);
console.log(arr.display());
```

## Time Complexity of Array Operations

| Operation                 | Typical Time Complexity |
|---------------------------|-------------------------|
| Access by index           | \(O(1)\)                |
| Update by index           | \(O(1)\)                |
| Search by value           | \(O(n)\)                |
| Insert at the end         | \(O(1)\) amortized      |
| Insert at the beginning   | \(O(n)\)                |
| Delete from the beginning | \(O(n)\)                |
| Iterate through the array | \(O(n)\)                |

---

```ts
// TypeScript Arrays: shift(), unshift(), splice() and slice()

// shift() — Remove the first element Removes the first element and returns it. The original array changes.
const numbers: number[] = [10, 20, 30, 40];
const removed = numbers.shift();
console.log(removed);


// unshift() — Add elements to the beginning
// Adds one or more elements to the start of an array. The original array changes.
const numbers: number[] = [20, 30, 40];
const length = numbers.unshift(5, 10);
console.log(numbers);
console.log(length);
```

# TypeScript Data Structures: Arrays

## `splice()` vs `slice()`

| Feature | `splice()` | `slice()` |
|---|---|---|
| Main purpose | Add, remove, replace | Extract or copy |
| Changes original array? | Yes | No |
| Return value | Array of removed elements | New array of selected elements |
| Parameters | Start, delete count, optional items | Start, optional end |
| Typical time complexity | `O(n)` | `O(k)`, where `k` is the number of elements copied |

## Array Operations: Time Complexity

| Operation | Method | Time Complexity | Explanation |
|---|---|---|---|
| Access by index | `arr[i]` | `O(1)` | Direct access using an index |
| Update by index | `arr[i] = value` | `O(1)` | Updates an element at a known index |
| Search by value | `indexOf()` | `O(n)` | May examine every element |
| Add to the end | `push()` | `O(1)` amortized | Usually adds one element; resizing can take `O(n)` |
| Remove from the end | `pop()` | `O(1)` | Removes the last element |
| Add to the beginning | `unshift()` | `O(n)` | Existing elements shift right |
| Remove from the beginning | `shift()` | `O(n)` | Remaining elements shift left |
| Insert at an arbitrary index | `splice()` | `O(n)` | Elements may need to shift |
| Remove at an arbitrary index | `splice()` | `O(n)` | Elements may need to shift |
| Replace elements | `splice()` | `O(n)` | Shifting may be required |
| Extract a portion | `slice()` | `O(k)` | Copies `k` selected elements |
| Copy the whole array | `slice()` | `O(n)` | Copies all `n` elements |
| Iterate through an array | `for`, `for...of`, `forEach()` | `O(n)` | Visits each element |
| Transform elements | `map()` | `O(n)` | Processes every element |
| Filter elements | `filter()` | `O(n)` | Checks every element |
| Find an element | `find()` | `O(n)` worst case | May examine every element |
| Check whether an element exists | `includes()` | `O(n)` worst case | May examine every element |
| Count elements | `length` | `O(1)` | Reads the stored array length |
| Reverse an array | `reverse()` | `O(n)` | Reorders elements in place |
| Sort an array | `sort()` | Typically `O(n log n)` | Depends on the JavaScript engine and input |

## Big O Notation

- `O(1)` — Constant time
- `O(log n)` — Logarithmic time
- `O(n)` — Linear time
- `O(n log n)` — Linearithmic time
- `O(n²)` — Quadratic time

**Notes:**
- `n` is the total number of elements in the array.
- `k` is the number of elements copied by `slice()`.
- `push()` is `O(1)` amortized, but an individual operation can take `O(n)` when resizing occurs.
- The time complexity of `splice()` depends on the starting index, the number of elements removed, and the number inserted. `O(n)` is the general worst-case bound.
- JavaScript engine implementations can affect the performance of certain operations.

