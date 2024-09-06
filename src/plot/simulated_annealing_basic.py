import numpy as np
import time
from scipy.stats import uniform

def schaffer_no_1(x1, x2):
    return 0.5 + ((np.sin((x1**2 + x2**2)**2))**2 - 0.5) / (1 + 0.001 * ((x1**2 + x2**2)**2))

def objective_function(x):
    return schaffer_no_1(x[0], x[1])

def simulated_annealing(f, bounds, initial_temperature, final_temperature, max_iterations):
    n = len(bounds)
    
    x = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
    best_x = x.copy()
    best_f = f(best_x)
    
    temperature = initial_temperature
    
    results = []
    
    for _ in range(max_iterations):
        new_x = x + np.random.normal(0, 0.1, size=n)
        new_x = np.clip(new_x, bounds[:, 0], bounds[:, 1])
        
        delta_f = f(new_x) - f(x)
        
        if delta_f <= 0:
            x = new_x
            if f(x) < best_f:
                best_x = x.copy()
                best_f = f(x)
        else:
            probability = np.exp(-delta_f / temperature)
            if np.random.rand() < probability:
                x = new_x
                if f(x) < best_f:
                    best_x = x.copy()
                    best_f = f(x)
        
        results.append({
            'temperature': temperature,
            'function_value': f(x),
            'best_function_value': best_f,
            'error_abs_min': abs(f(x) - 0),
            'error_dist_min': np.linalg.norm(x - np.array([0, 0])),
            'optimal_point': best_x.tolist(),
        })
        
        temperature *= 0.99
        
        if temperature <= final_temperature:
            break
    
    return results

dimensions = 2
bounds = np.array([[-10, 10]] * dimensions)

initial_temperature = 1000
final_temperature = 0.01
max_iterations = 100000

results = []

for _ in range(20):
    start_time = time.time()
    result = simulated_annealing(objective_function, bounds, initial_temperature, final_temperature, max_iterations)
    end_time = time.time()
    
    # Calculate the average function value
    duration_error = np.mean([r['function_value'] for r in result])
    duration_std = np.std([r['function_value'] for r in result])
    
    # Calculate the mean errors
    abs_min_error_mean = np.mean([r['error_abs_min'] for r in result])
    dist_min_error_mean = np.mean([r['error_dist_min'] for r in result])
    
    # Append the result to the overall results list
    results.append({
        'duration': end_time - start_time,
        'abs_min_error_mean': abs_min_error_mean,
        'dist_min_error_mean': dist_min_error_mean,
        'duration_std': duration_std,
        'last_optimal_point': result[-1]['optimal_point']
    })

# Print the results
print("Resultados de las 20 ejecuciones:")
for i, result in enumerate(results, 1):
    print(f"Ejecución {i}:")
    print(f"Duración: {result['duration']:.4f} segundos")
    print(f"Error absoluto promedio respecto al mínimo real: {result['abs_min_error_mean']:.6f}")
    print(f"Distancia euclidiana promedio respecto al punto óptimo real: {result['dist_min_error_mean']:.6f}")
    print(f"Diferencia estándar de la duración: {result['duration_std']:.6f}")
    print(f"Punto óptimo encontrado: {result['last_optimal_point']} en {objective_function(result['last_optimal_point'])}")
    print()

# Calcula estadísticas finales
total_duration = sum(r['duration'] for r in results) / len(results)
avg_abs_min_error = np.mean([r['abs_min_error_mean'] for r in results])
avg_dist_min_error = np.mean([r['dist_min_error_mean'] for r in results])

print("\nEstadísticas finales:")
print(f"Duración media total: {total_duration:.4f} segundos")
print(f"Error absoluto promedio respecto al mínimo real: {avg_abs_min_error:.6f}")
print(f"Distancia euclidiana promedio respecto al punto óptimo real: {avg_dist_min_error:.6f}")