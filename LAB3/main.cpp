#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;
    Node(int x, Node *n) {data=x; next=n;}
};

class Queue {
private:
    Node *front, *rear;
    int size;
public:
    Queue() {
        front = rear = NULL;
        size = 0;
    }
    void enqueue(int x) {
        Node *temp = new Node(x, NULL);
        if (rear == NULL) {
            front = rear = temp;
        } else {
            rear->next = temp;
            rear = temp;
        }
        size++;
    }
    void dequeue() {
        if (front == NULL) {
            cout << "Queue is empty.." << endl;
            return;
        }
        Node *temp = front;
        front = front->next;
        delete temp;
        size--;
        if (front == NULL) {
            rear = NULL;
        }
    }
    int top() {
        if (front == NULL) {
            cout << "Queue is empty.." << endl;
            return -1;
        }
        return front->data;
    }
    int getSize() {
        return size;
    }
    bool isEmpty() {
        return (front == NULL);
    }
};
class Stack{
private:
    Node *top;
    int size;public:
public:
    void push(int a){
        Node *temp = new Node(a, top);
        top = temp;
        size++;
    };
    void pop() {
        if (top == NULL) {
            cout << "Stack is empty..." << endl;
            return;
        }
        Node *temp = top;
        top = top->next;
        delete temp;
        size--;
    }
    int getTopValue() {
        if (top == NULL) {
            cout << "Stack is empty" << endl;
            return -1;
        }
        return top->data;
    }
    int getSize() {
        return size;
    }
    bool isEmpty() {
        return (top == NULL);
    }
};

int main() {
    //This line is for queue implementation
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << "Queue size is " << q.getSize() << endl;
    cout << "Front element is " << q.top() << endl;
    q.dequeue();
    cout << "Queue size is " << q.getSize() << endl;
    cout << "Front element is " << q.top() << endl;
    q.dequeue();
    q.dequeue();
    if (q.isEmpty()) {
        cout << "Queue is empty" << endl;
    } else {
        cout << "Queue is not empty" << endl;
    }


    //This line is for stack implementation
    Stack s;
    s.push(1);
    s.push(2);
    s.push(3);
    cout << "Stack size is " << s.getSize() << endl;
    cout << "Top element is " << s.getTopValue() << endl;
    s.pop();
    cout << "Stack size is " << s.getSize() << endl;
    cout << "Top element is " << s.getTopValue() << endl;
    s.pop();
    s.pop();
    if (s.isEmpty()) {
        cout << "Stack is empty" << endl;
    } else {
        cout << "Stack is not empty" << endl;
    }
    return 0;}
