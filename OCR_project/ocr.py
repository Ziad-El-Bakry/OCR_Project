import easyocr
import time
import os
import datetime

def perform_ocr(image_path, languages=['en']):
    # Initialize the OCR reader (first time will download the model files)
    print(f"Initializing EasyOCR reader for languages: {', '.join(languages)}...")
    reader = easyocr.Reader(languages)
    
    # Read the image and perform OCR
    print(f"\nProcessing image: {image_path}")
    start_time = time.time()
    
    results = reader.readtext(image_path)
    
    end_time = time.time()
    print(f"Processing time: {end_time - start_time:.2f} seconds")
    
    # Get combined text for easy use
    combined_text = " ".join([detection[1] for detection in results])
    print("\nCombined Text:")
    print(combined_text)
    
    # Create output directory if it doesn't exist
    output_dir = "ocr_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    # Create output file name based on input image name
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{base_name}_{timestamp}.txt")
    
    # Save combined text to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_text)
    
    print(f"\nCombined text saved to: {output_file}")
    
    # Print individual text segments with confidence scores for detailed info
    print("\nDetailed Results:")
    for detection in results:
        text = detection[1]  # The detected text
        confidence = detection[2]  # Confidence score
        print(f"Text: {text} (Confidence: {confidence:.2f})")
    
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    print("OCR (Optical Character Recognition) Tool")
    print("========================================")
    
    # Ask user for image path
    image_path = input("\nEnter the path to the image you want to process: ")
    
    # Check if file exists
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' not found.")
        # Suggest images in test_images folder if it exists
        if os.path.isdir("test_images"):
            print("\nAvailable images in test_images folder:")
            for img in sorted([f for f in os.listdir("test_images") if f.lower().endswith(('.png', '.jpg', '.jpeg'))]):
                print(f"  - test_images/{img}")
            print("\nTry again with one of these paths.")
        exit(1)
    
    # Ask user for language preference
    print("\nLanguage options:")
    print("1. English only")
    print("2. Arabic only")
    print("3. Both English and Arabic")
    
    while True:
        lang_choice = input("\nEnter your choice (1-3): ")
        if lang_choice == "1":
            languages = ['en']
            break
        elif lang_choice == "2":
            languages = ['ar']
            break
        elif lang_choice == "3":
            languages = ['en', 'ar']
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    # Perform OCR with selected languages
    perform_ocr(image_path, languages) 