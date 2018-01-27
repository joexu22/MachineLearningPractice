# MNSIT
* Modified National Institute of Standards and Technology
* Large Database of Handwritten Digits
* Commonly used for various image processing systems
* ML intro

# Normalizating and Centering Machine
* IDEA: General ML Approach to Finding the Balance "Point" of 2D Images...
* [Input] -> Mathmatically Generated Images
  * Create images using "principled" geometry -> (axioms, point, line, plan, etc...)
  * Apply Symmetry about (some "known" marker)
    * Reflection, Rotation, Translational, Helical, Scale, *Glide, *Improper
    * Helical: Map 2D -> 3D
    * Examine -> (Mandelbrot)?
    * Non-Euclidean Geometry...
  * (Apply Noise?): Combine Transformations In Random Manners
    * Mathmatically tracking ("known" marker) along each transformation
* [Input] -> Further Generation of Random Images
  * Use Random Scribbles as base
  * Apply -> Same Symmetical Principles to Scribble
    * Tracking the "known" point of symmetry
* Create Optimizer
  * Optimize - A ML_Model that calculates the Center Point
    * Reduce "ML-calculated" center from "known" mathmatical center
    * The ML_Model should be able to find the exact center each time
    * Mathmatically there exists a "correct" answer
      * Train machine to see the center point without prior knowledge of transforms
  * Training
    * Train ML to find center [of a image with "known" center]
    * Train ML to find next center (new image) [with "known" center]
    * How much the center is off by should be decreasing...
    * [Practical Application]
      * Feed it a image "without" known center, it should give you a relatively good guess as to where the center is

* Applications
  * [Photocopy Some Historical Journal] - Normalize some Historical Figures hand writing
  * [How Handwriting is Normalized?] - Technically handwritting is a 3D object in 2D (Even Paint has Thinkness)
  * Further Uses: Generating One's Own "MNIST"
  * Further Uses: - [Cubist Thing: (Maping 3D objects back into 2D space) and easier identification of 2D space]

* Future Work
  * Find Line of Balance
  * Find Plane of Balance, etc. etc. etc.