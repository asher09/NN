def objective_function(x):
    return -x**2 + 4*x

def hill_climbing(start, step):
    current_x = start
    current_value = objective_function(current_x)
    while True: 
        next_x = current_x + step
        next_value = objective_function(next_x)

        if next_value > current_value:
            current_x = next_x
            current_value = next_value
        else:
            break
    return current_x, current_value

best_x, best_value = hill_climbing(start=0, step=0.1)
print(f"Best solution: x = {best_x}, f(x) = {best_value}")