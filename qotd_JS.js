// in js



// def string_bits(string):
//     newString = ''
//     for char in range(len(string)):
//         if char % 2 == 0:
//             #print(string[char])
//             newString = newString + string[char]
//             #print(newString)
//     return newString


function string_bits(string) {
    let new_string = '';
    for (var i = 0; i < string.length; i++) {
        if (i % 2 == 0) {
            new_string += string[i]
            //console.log(new_string);
        }
        //  console.log(new_string);
    }
    return new_string
}
