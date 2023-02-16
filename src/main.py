import generate_data as data


if __name__ == '__main__':
    for i in range(40):
        total = data.total_average("Estudiante")
        partial = data.partial_average("Estudiante", total)
        print(total)

