from django.db import models

class MedicalData(models.Model):
    # Patient Data
    FullName=models.CharField(max_length=50)
    uhid= models.CharField(max_length=20)
    refby=models.CharField(max_length=100)
    age=models.CharField(max_length=50)
    mobileNo=models.CharField(max_length=20)
    date = models.CharField(max_length=10)

    BronchoVascularMarking=models.CharField(max_length=10)
    BronchoVascularMarkingSide = models.CharField(max_length=10, blank=True, null=True)
    BronchoVascularMarkingRegion = models.CharField(max_length=30, blank=True, null=True)

    opacity=models.CharField(max_length=10)
    opacitySide = models.CharField(max_length=10, blank=True, null=True)
    opacityRegion = models.CharField(max_length=30, blank=True, null=True)


    # Cavity
    cavity = models.CharField(max_length=10)
    cavitySide = models.CharField(max_length=10, blank=True, null=True)
    cavityRegion = models.CharField(max_length=30, blank=True, null=True)

    # Masses
    masses = models.CharField(max_length=10)
    massesSide = models.CharField(max_length=10, blank=True, null=True)
    massesRegion = models.CharField(max_length=30, blank=True, null=True)

    # Hilum
    hilum = models.CharField(max_length=10)
    hilumSide = models.CharField(max_length=10)
    ProminentHilumSpecify = models.CharField(max_length=30, blank=True, null=True)

    trachea = models.CharField(max_length=10)
    tracheaShiftSide = models.CharField(max_length=10, blank=True, null=True)


    # Mediastinum
    mediastinal = models.CharField(max_length=10)
    mediastinalShiftSide = models.CharField(max_length=10, blank=True, null=True)

    # Lymph Nodes
    LymphNodes = models.CharField(max_length=10)

    # Cardiac
    CardiacSize = models.CharField(max_length=10)
    CardiacShape = models.CharField(max_length=10)
    CardiacShapeAbnormal = models.CharField(max_length=30, blank=True, null=True)
    AorticKnuckle = models.CharField(max_length=10)
    AorticKnuckleCalcification = models.CharField(max_length=10)
    AorticKnuckleUnfoldingofAorta = models.CharField(max_length=10)

    CostophrenicAngles = models.CharField(max_length=10)
    CostophrenicAnglesSide = models.CharField(max_length=10, blank=True, null=True)

    # Pleura
    Pneumothorax = models.CharField(max_length=10)
    PneumothoraxSide = models.CharField(max_length=10, blank=True, null=True)

    # Chest Wall
    BonyCage = models.CharField(max_length=10)
    BonyCageSide = models.CharField(max_length=10, blank=True, null=True)
    Finding = models.CharField(max_length=30, blank=True, null=True)
    Bonylesion = models.CharField(max_length=10, blank=True, null=True)
    # fracture = models.BooleanField(default=False)
    FractureSide = models.CharField(max_length=10, blank=True, null=True)
    FractureRibNumber = models.PositiveSmallIntegerField(blank=True, null=True)
    SoftTissue = models.CharField(max_length=10)
    SoftTissueSide = models.CharField(max_length=10, blank=True, null=True)
    SoftTissueAbnormal = models.CharField(max_length=30, blank=True, null=True)

    # Diaphragm
    HemiDiaphragmSide = models.CharField(max_length=10)
    HemiDiaphragm = models.CharField(max_length=10)
    HemiDiaphragmAbormal = models.CharField(max_length=30, blank=True, null=True)

    # Breast Shadow
    BreastShadow = models.CharField(max_length=10)
    BreastShadowSide = models.CharField(max_length=10, blank=True, null=True)
    BreastShadowAbnormal = models.CharField(max_length=30, blank=True, null=True)