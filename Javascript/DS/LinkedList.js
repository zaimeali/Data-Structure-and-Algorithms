class Node {
    constructor(data, next = null) {
        this.data = data
        this.next = next
    }
}

class LinkedList {
    constructor() {
        this.head = null
        this.size = 0
    }

    // Insert First Node
    insertFirst(data) {
        this.head = new Node(data, this.head)
        this.size++
    }

    // Insert Last Node
    insertLast(data) {
        let node = new Node(data)
        let current

        // If Empty then make it head
        if(!this.head) {
            this.head = node
        } else {
            current = this.head
            while(current.next) {
                current = current.next
            }
            current.next = node
        }

        this.size++
    }


    // Insert at Index
    insertAt(data, index) {
        // if index out of range
        if(index > 0 && index > this.size) {
            return
        }

        // if first index
        if(index === 0) {
            this.insertFirst(data)
            return
        }

        const node = new Node(data)
        let current, previous

        // Set current to first
        current = this.head
        let count = 0
        
        while(count < index) {
            previous = current // node before index
            count++
            current = current.next // node after index
        }

        node.next = current
        previous.next = node

        this.size++
    }

    // Get at Index
    getAt(index) {
        let current = this.head
        let count = 0

        while(current) {
            if(count == index) {
                console.log(current.data)
                return
            }
            count++
            current = current.next
        }

        return null
    }


    // Remove at Index
    removeAt(index) {
        if(index > 0 && index > this.size) {
            return 
        }

        let current = this.head
        let previous
        let count = 0

        if(index === 0) {
            this.head = current.next
        } else {
            while(count < index) {
                count++
                previous = current
                current = current.next
            }
            previous.next = current.next
        }

        this.size--
    }

    // Clear List
    clearList() {
        this.head = null
        this.size = 0
    }


    // Print List Data
    printListData() {
        let current = this.head
        while(current) {
            console.log(current.data)
            current = current.next
        }
    }
}

const link = new LinkedList()
link.insertFirst(100)
link.insertFirst(200)
link.insertFirst(300)
link.insertLast(400)
link.insertAt(500, 2)
link.insertAt(800, 0)
link.insertAt(900, 10)  // test case because 10 is not in length


// link.printListData()

// console.log("Get by Index")
// link.getAt(3)

// link.removeAt(3)
// link.printListData()

link.clearList()
link.printListData()