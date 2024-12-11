def merge_and_remove_duplicates(list1, list2):

    combined_list = list1 + list2

    merged_list = list(set(combined_list))
    
    return merged_list

def main():
    while True:
        user_input = input("Enter two lists of numbers separated by spaces (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        try:
            list1_str, list2_str = user_input.split()
            
            list1 = [int(item) for item in list1_str.split(',')]
            list2 = [int(item) for item in list2_str.split(',')]
            
            merged_list = merge_and_remove_duplicates(list1, list2)
            
            print("Merged list without duplicates:", merged_list)
        
        except ValueError:
            print("Please enter the lists in the correct format (e.g., '1,2,4,6 2,5,7,1').")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()