var groupmates = [
    {
        "name": "Диана",
        "group": "bst2253",
        "age": 29,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Ольга",
        "group": "bst2253",
        "age": 23,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": "Игорь",
        "group": "bst2257",
        "age": 25,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": "Дмитрий",
        "group": "bst2257",
        "age": 26,
        "marks": [5, 5, 5, 4, 5]
    }
];

console.log(groupmates);
var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length) {
        str = str + ' ';
    }
    return str;
};

var printStudents = function(students) {
    console.log(
        rpad("Имя студента", 15),
        rpad("Группа", 8),
        rpad("Возраст", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++) {
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['age'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

printStudents(groupmates);
var filterByGroup = function(students, group) {
    var filtered = [];
    for (var i = 0; i < students.length; i++) {
        if (students[i]['group'] === group) {
            filtered.push(students[i]);
        }
    }
    return filtered;
};

// Пример использования:
var groupBst2253 = filterByGroup(groupmates, "bst2253");
console.log("Студенты группы bst2253:");
printStudents(groupBst2253);