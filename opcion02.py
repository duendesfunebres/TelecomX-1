def normalizacion ():
    from colorama import init, Fore, Back
    init(autoreset=True) 
    init()
    from collections import defaultdict
    import json


    with open('TelecomX.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    def analyze_columns(data):
        column_types = defaultdict(set)

        def detect_conversion(value):
            if isinstance(value, str):
                if value.lower() in {"yes", "no"}:
                    return "bool"
                try:
                    float(value)
                    return "float"
                except ValueError:
                    pass
            return type(value).__name__

        def recursive_scan(prefix, obj):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_prefix = f"{prefix}.{key}" if prefix else key
                    recursive_scan(new_prefix, value)
            else:
                tipo = detect_conversion(obj)
                column_types[prefix].add(tipo)

        for record in data:
            recursive_scan("", record)

        return column_types

    def display_column_analysis(data):
        column_types = analyze_columns(data)
        for col, types in column_types.items():
            type_list = ", ".join(sorted(types))
            print(f"- {col}: {type_list}")

    display_column_analysis(data)
    print ("")
    input("Presiona Enter para continuar...")  # ← Aquí se pausa
