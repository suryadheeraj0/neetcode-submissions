interface Shape {
    Shape clone();
}

class Rectangle implements Shape {
    private int width;
    private int height;

    public Rectangle(int width, int height) {
        this.width = width;
        this.height = height;
    }

    public int getWidth() {
        return this.width;
    }

    public int getHeight() {
        return this.height;
    }

    @Override
    public Shape clone() {
        return new Rectangle(this.width,this.height);
    }
}

class Square implements Shape {
    private int length;

    public Square(int length) {
        this.length = length;
    }

    public int getLength() {
        return this.length;
    }

    @Override
    public Shape clone() {
        return new Square(this.length);
    }
}

class Test {
    public List<Shape> cloneShapes(List<Shape> shapes) {
        List<Shape> list = new ArrayList<>();
        Shape square = new Square(10);
        Shape anotherSquare = square.clone();
        Shape rectangle = new Rectangle(10, 20);
        Shape anotherRectangle = rectangle.clone();
        list.add(square);
        list.add(rectangle);
        list.add(anotherSquare);
        list.add(anotherRectangle);
        return list;
    }
}
