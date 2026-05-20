import Input_handler, output_handler, eval_expression  # Импорт модулей

def main():  # Определение порядка действий
    a, b, action = Input_handler.input_expression() 
    result = eval_expression.eval_expression(a, b, action)
    output_handler.output_result(a, b, action, result)

if __name__ == "__main__":  # Запуск программы
main()