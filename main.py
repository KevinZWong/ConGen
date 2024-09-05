from ConcurrentGeneration import ConcurrentImageProcessing
image_descriptions = [
    "A large, fluffy Golden Retriever running across a grassy field, sunlight glinting off its silky golden fur, tongue lolling out, and tail wagging enthusiastically, capturing its joyful and playful nature.",
    "A sleek, striking Siberian Husky dashing through a snow-covered forest, its ice-blue eyes focused ahead, muscles rippling under its thick fur coat as it effortlessly cuts through the snowy landscape.",
    "A small, long-bodied Dachshund scampering through a backyard, its short legs moving quickly beneath it, with its floppy ears bouncing and shiny brown coat gleaming in the afternoon light.",
    "An elegant Standard Poodle prancing gracefully down a city sidewalk, its tight, curly white coat bouncing with each step, perfectly groomed, exuding confidence and poise with its head held high.",
    "A high-energy Border Collie darting through a field, intensely focused on herding sheep, its sleek black and white coat shimmering in the sunlight as it moves with agility and precision."
]

concurrent_images = ConcurrentImageProcessing("ImageGenerationOOP.py")

print(concurrent_images.generate_images(image_descriptions, "output/image_"))


