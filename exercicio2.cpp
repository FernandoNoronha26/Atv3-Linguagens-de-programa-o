#include <iostream>
#include <stack>

int main() {
    // Criando uma pilha vazia
    std::stack<int> pilha;

    // Adicionando elementos à pilha
    pilha.push(10);
    pilha.push(20);
    pilha.push(30);

    // Exibindo os elementos da pilha
    std::cout << "Elementos da pilha: ";
    while (!pilha.empty()) {
        std::cout << pilha.top() << ", ";
        pilha.pop();
    }
    std::cout << std::endl;

    return 0;
}