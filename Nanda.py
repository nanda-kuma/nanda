import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to perform image recognition and extract text
def image_to_text(image_path):
    try:
        # Load the image using OpenCV
        image = cv2.imread(image_path)

        # Validate if image exists
        if image is None:
            raise ValueError("Error: Unable to load image. Please check the path.")

        # Convert the image to grayscale for better OCR accuracy
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding to improve text visibility
        thresh_image = cv2.adaptiveThreshold(
            gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        # Use pytesseract to extract text from the image
        text = pytesseract.image_to_string(thresh_image)

        return text.strip()  # Remove extra spaces and new lines
    except Exception as e:
        return f"Error: {e}"

# Main function
def main():
    # Get the image path from user input
    image_path = input("Enter the path to the image: ").strip()

    # Extract text from the image
    extracted_text = image_to_text(image_path)

    if not extracted_text:
        print("No readable text found in the image.")
    else:
        print("\nExtracted Text:\n" + extracted_text)

# Run the program
if __name__ == "__main__":
    main()
