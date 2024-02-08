import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_test import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from infix_postfix_conversion import infix_to_postfix, Stack
from dq import Node, Queue, Deque
from hashtable import Hashtable, process_commands, generate_table
from train_network import get_shortest_route, Graph, get_shortest_route_distance
import sorting_algorithm
import random


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('group_profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
    return render_template('contacts.html')


@app.route('/work1', methods=['GET', 'POST'])
def work1():
    return render_template('work1.html')


@app.route('/work2', methods=['GET', 'POST'])
def work2():
    return render_template('work2.html')


@app.route('/work3', methods=['GET', 'POST'])
def work3():
    return render_template('work3.html')


@app.route('/work4', methods=['GET', 'POST'])
def work4():
    return render_template('work4.html')


@app.route('/work5', methods=['GET', 'POST'])
def work5():
    return render_template('work5.html')


@app.route('/work6', methods=['GET', 'POST'])
def work6():
    return render_template('work6.html')


@app.route('/bubble')
def bubble():
    return render_template('bubblesortalgo.html')


@app.route('/bubblesort')
def bubble_sort():
    return render_template('bubblesort.html')


@app.route('/bubblesort2')
def bubble_sort2():
    return render_template('bubblesort2.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route("/smallalgo", methods=["GET", "POST"])
def small_algo():
    
    numbers = range(1, 101)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/mediumalgo", methods=["GET", "POST"])
def medium_algo():
    
    numbers = range(1, 1001)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1)  * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/largealgo", methods=["GET", "POST"])
def large_algo():
    
    numbers = range(1, 10001)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
    })


@app.route('/infix-postfix', methods=['GET', 'POST'])
def infix():
    result = None
    if request.method == 'POST':
        infix_notation = request.form.get('infix', '')
        postfix = infix_to_postfix(infix_notation)

        steps = ""

        for i in range(len(postfix) + 1):
            steps += (''.join(postfix[:i]) + "\n")

        result = f"Processed Conversion: {steps}\nOutput Postfix: \n{postfix}"

    return render_template('infixpostfix.html', result=result)


global_queue = Queue()


@app.route("/queue", methods=["GET", "POST"])
def queue():
    global global_queue
    linked_list_data = []

    if request.method == "POST":
        usage = request.form.get("usage")

        if usage == "enqueue":
            data_to_add = request.form.get("data")
            global_queue.enqueue(data_to_add)
            linked_list_data = global_queue.printLinkedList()
            print("Linked List Data:", linked_list_data)

        elif usage == "dequeue":
            global_queue.dequeue()
            linked_list_data = global_queue.printLinkedList()
            print("Linked List Data:", linked_list_data)
    return render_template("Queue.html", linked_list_data=linked_list_data)


global_deque = Deque()


@app.route("/deque", methods=["GET", "POST"])
def deque():
    global global_deque
    linked_list_data = []

    if request.method == "POST":
        usage = request.form.get("usage")

        if usage == "add front":
            data_to_add = request.form.get("data")
            global_deque.add_front(data_to_add)
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)
        elif usage == "add rear":
            data_to_add = request.form.get("data")
            global_deque.add_rear(data_to_add)
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)
        elif usage == "remove front":
            global_deque.remove_front()
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)
        elif usage == "remove rear":
            global_deque.remove_rear()
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)
    return render_template("Deque.html", linked_list_data=linked_list_data)


@app.route('/hashtable', methods=['GET', 'POST'])
def hash_table():
    if request.method == 'POST':
        selected_hash_function = request.form['hash_function']
        num_commands = int(request.form['num_commands'])
        commands = request.form['commands'].split('\n')

        if selected_hash_function == 'hash_function_1':
            process_commands(commands, 1)
        elif selected_hash_function == 'hash_function_2':
            process_commands(commands, 2)
        elif selected_hash_function == 'hash_function_3':
            process_commands(commands, 3)

    sample_table = generate_table()
    return render_template('hashtable.html', output=sample_table)


@app.route("/train_network", methods=["GET", "POST"])
def train_network():
    if request.method == "POST":
        starting_station = request.form.get("starting_station")
        target_station = request.form.get("target_station")
        try:
            rail_system = Graph()
            rail_system.add_edge("Recto", "Legarda", 1.05)
            rail_system.add_edge("Legarda", "Pureza", 1.389)
            rail_system.add_edge('Recto', 'Legarda', 1.05)
            rail_system.add_edge('Legarda', 'Pureza', 1.389)
            rail_system.add_edge('Pureza', 'V. Mapa', 1.357)
            rail_system.add_edge('V. Mapa', 'J. Ruiz', 1.234)
            rail_system.add_edge('J. Ruiz', 'Gilmore', 0.928)
            rail_system.add_edge('Gilmore', 'Betty Go', 1.075)
            rail_system.add_edge('Betty Go', 'Cubao LRT Line', 1.164)
            rail_system.add_edge('Cubao LRT Line', 'Anonas', 1.438)
            rail_system.add_edge('Anonas', 'Katipunan', 0.955)
            rail_system.add_edge('Katipunan', 'Santolan', 1.97)
            rail_system.add_edge('Santolan', 'Marikina Pasig', 1.66)
            rail_system.add_edge('Marikina Pasig', 'Antipolo', 2.35)

            # Line 1
            rail_system.add_edge('Baclaran', 'Edsa', 0.588)
            rail_system.add_edge('Edsa', 'Libertad', 1.01)
            rail_system.add_edge('Libertad', 'Gil Puyat', 0.73)
            rail_system.add_edge('Gil Puyat', 'Vito Cruz', 1.061)
            rail_system.add_edge('Vito Cruz', 'Quirino', 0.827)
            rail_system.add_edge('Quirino', 'Pedro Gil', 0.794)
            rail_system.add_edge('Pedro Gil', 'United Nations Avenue', 0.754)
            rail_system.add_edge('United Nations Avenue', 'Central Terminal', 1.214)
            rail_system.add_edge('Central Terminal', 'Carriedo', 0.725)
            rail_system.add_edge('Carriedo', 'Doroteo Jose', 0.685)
            rail_system.add_edge('Doroteo Jose', 'Recto', 0.352)
            rail_system.add_edge('Doroteo Jose', 'Bambang', 0.648)
            rail_system.add_edge('Bambang', 'Tayuman', 0.618)
            rail_system.add_edge('Tayuman', 'Blumentritt', 0.671)
            rail_system.add_edge('Blumentritt', 'Abad Santos', 0.927)
            rail_system.add_edge('Abad Santos', 'R. Papa', 0.66)
            rail_system.add_edge('R. Papa', '5th Avenue', 0.954)
            rail_system.add_edge('5th Avenue', 'Monumento', 1.087)
            rail_system.add_edge('Monumento', 'Balintawak', 2.25)
            rail_system.add_edge('Balintawak', 'Roosevelt', 1.87)

            # MRT
            rail_system.add_edge('Roosevelt', 'North Ave', 1.42)
            rail_system.add_edge('North Ave', 'Quezon Ave', 0.936)
            rail_system.add_edge('Quezon Ave', 'GMAKamuning', 1.951)
            rail_system.add_edge('GMAKamuning', 'Cubao MRT Line', 1.405)
            rail_system.add_edge('Cubao MRT Line', 'Cubao LRT Line', 0.551)
            rail_system.add_edge('Cubao MRT Line', 'Santolan-Annapolis', 2.334)
            rail_system.add_edge('Santolan-Annapolis', 'Ortigas', 0.797)
            rail_system.add_edge('Ortigas', 'Shaw Boulevard', 0.988)
            rail_system.add_edge('Shaw Boulevard', 'Boni', 0.83)
            rail_system.add_edge('Boni', 'Guadalupe', 1.924)
            rail_system.add_edge('Guadalupe', 'Buendia', 0.886)
            rail_system.add_edge('Buendia', 'Ayala', 1.201)
            rail_system.add_edge('Ayala', 'Magallanes', 1.941)
            rail_system.add_edge('Magallanes', 'Taft Ave', 0.131)
            rail_system.add_edge('Taft Ave', 'Edsa', 0.289)

            alternate_routes = rail_system.alternate_routes(starting_station, target_station)
            result = get_shortest_route(alternate_routes)
            distance = get_shortest_route_distance(alternate_routes)
            return render_template('train_network.html', result=result, distance=round(distance, 2))
        except ValueError:
            return render_template("train_network.html")
    return render_template('train_network.html')


@app.route('/sorting_algo', methods=['GET', 'POST'])
def sort():
    random_numbers = [random.randint(0, 1000) for _ in range(1000)]
    random_numbers = ", ".join(map(str, random_numbers))

    if request.method == 'POST':
        integer_list = request.form.get("num-list")
        try:
            sorting_type = request.form.get("sorting_type")
            input_list = [float(x.strip()) for x in integer_list.split(',')]

            if sorting_type == "bubble_sort":
                start_time = timeit.default_timer()
                result = sorting_algorithm.bubble_sort(input_list)
                execution_time = timeit.default_timer() - start_time
                return render_template('sorting.html', result=result, time=execution_time)
            elif sorting_type == "selection_sort":
                start_time = timeit.default_timer()
                result = sorting_algorithm.selection_sort(input_list)
                execution_time = timeit.default_timer() - start_time
                return render_template('sorting.html', result=result, time=execution_time)
            elif sorting_type == "insertion_sort":
                start_time = timeit.default_timer()
                result = sorting_algorithm.insertion_sort(input_list)
                execution_time = timeit.default_timer() - start_time
                return render_template('sorting.html', result=result, time=execution_time)
            elif sorting_type == "merge_sort":
                start_time = timeit.default_timer()
                result = sorting_algorithm.merge_sort(input_list)
                execution_time = timeit.default_timer() - start_time
                return render_template('sorting.html', result=result, time=execution_time)
            elif sorting_type == "quick_sort":
                start_time = timeit.default_timer()
                result = sorting_algorithm.quick_sort(input_list)
                execution_time = timeit.default_timer() - start_time
                return render_template('sorting.html', result=result, time=execution_time)
        except:
            return ValueError
    return render_template('sorting.html', random_integers=random_numbers)


if __name__ == "__main__":
    app.run(debug=True)
