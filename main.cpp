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

int main() {
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
    return 0;
}
