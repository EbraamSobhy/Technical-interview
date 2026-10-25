const user = {
    name: "Pero"
};

function greet() {
    console.log(`Hello I'm ${this.name}`);
}

const newUser = greet.bind(user);

newUser();

