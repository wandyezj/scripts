import {hello} from "../../src/index"

console.log(hello());

function testHello() {
    return hello();
}

// place tests on global window object to break out of compiled module
const win = (window as unknown) as Window &
    {
        tests: {[key: string]: () => any};
    };

win.tests = {};
win["tests"].testHello = testHello;
