class Anemia:
    positiveResult = 'The patient is Anemic'
    negativeResult = 'The patient is norAnemic'
    AnemiaResult = ''
    def checkAnemia(self, Sex, Red_Blood_Cell, White_Blood_Cell, Platelets, Hemoglobin):
        test1 = Sex ==1.0 and 4000000.0 <= Red_Blood_Cell <=5000000.0 and 4000.0 <= White_Blood_Cell <=11000.0 and 150000.0<= Platelets <=400000.0 and 11.0<= Hemoglobin <=16.0
        test2 = Sex ==0.0  and 3650000.0 <= Red_Blood_Cell <=4500000.0 and 4000.0 <= White_Blood_Cell <=11000.0 and 150000.0<= Platelets <=400000.0 and 10.0<= Hemoglobin <=15.0
        test3 = Sex ==1.0 and Red_Blood_Cell <4000000.0 and Hemoglobin<11.0
        test4 = Sex ==0.0 and Red_Blood_Cell <3650000.0 and Hemoglobin<10.0

        if test1 or test2:
            self.AnemiaResult = self.negativeResult
        elif test3 or test4:
            self.AnemiaResult = self.positiveResult
        else:
            self.AnemiaResult = self.positiveResult#'invalid input'

        return self.AnemiaResult
    
class Diabetes:
    case1 = 'The patient is normal'
    case2 = 'The patient is Impaired Glucose'
    case3 = 'The patient is Diabetic'
    case4 = 'The patient is in a diabetic coma'
    
    diabetesResult = ''

    def checkTheCase(self, Fasting, After_Eating, Hours_After_Eating):
        #diabetes tests boolean variables
        test1 = 80.0 <= Fasting.data <= 100.0 and 170.0 <= After_Eating.data <= 200.0 and 120.0 <= Hours_After_Eating.data <= 140.0
        test2 = 101.0 <= Fasting.data <= 125.0 and 190.0 <= After_Eating.data <= 230.0 and 140.0 <= Hours_After_Eating.data <= 160.0
        test3 = Fasting.data >=126.0 and 220.0 <= After_Eating.data <= 300.0 and  Hours_After_Eating.data >= 200.0
        test4 = Fasting.data <80.0

        #the functionality 
        if test1:
            diabetesResult = self.case1
        elif test2:
            diabetesResult = self.case2
        elif test3:
            diabetesResult = self.case3
        elif test4:
            diabetesResult = self.case4
        else:
            diabetesResult = 'invalid inputs'
        
        return diabetesResult
    
class Kidney:
    case1 = 'The Kidney is Healthy'
    case2 = 'The Kidney is Tired'
    case3 = 'The Kidney need Dialysis'

    KidneyResult = ''

    def checkKidney(self, Creatinin, Creatinin_Clearance, Na, K, Cl, Blood_Urine_Nitrogen, Urea):
        CreatininHealthy = Creatinin.data >= 0.7 and Creatinin.data <= 1.4
        Creatinin_ClearanceHealthy = Creatinin_Clearance.data >= 97.0 and Creatinin_Clearance.data <= 137.0
        NaHealthy = Na.data >= 135.0 and Na.data <= 148.0
        KHealthy = K.data >= 3.5 and K.data <= 5.0
        ClHealthy = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenHealthy = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaHealthy = Urea.data >= 20.0 and Urea.data <= 40.0
        TestHealthy = CreatininHealthy and Creatinin_ClearanceHealthy and NaHealthy and KHealthy and ClHealthy and Blood_Urine_NitrogenHealthy and UreaHealthy
        #----------------------------------------------------------------------------------------------------
        CreatininTired = Creatinin.data >= 1.5  
        Creatinin_ClearanceTired = Creatinin_Clearance.data <=95.0
        NaTired = Na.data >= 135.0 and Na.data <= 148.0
        KTired = K.data >3.5 
        ClTired = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenTired = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaTired = Urea.data >= 40.0 and Urea.data <= 200.0
        TestTired = CreatininTired and Creatinin_ClearanceTired and NaTired and KTired and ClTired and Blood_Urine_NitrogenTired and UreaTired
        #----------------------------------------------------------------------------------------------------
        CreatininDialysis = Creatinin.data >7.0
        Creatinin_ClearanceDialysis = Creatinin_Clearance.data <= 15.0 
        NaDialysis = Na.data >= 135.0 and Na.data <= 148.0
        KDialysis = K.data >5.5
        ClDialysis = Cl.data >= 95.0 and Cl.data <= 105.0
        Blood_Urine_NitrogenDialysis = Blood_Urine_Nitrogen.data >= 7.0 and Blood_Urine_Nitrogen.data <= 20.0
        UreaDialysis = Urea.data >200.0
        TestDialysis = CreatininDialysis and Creatinin_ClearanceDialysis and NaDialysis and KDialysis and ClDialysis and Blood_Urine_NitrogenDialysis and UreaDialysis
        #----------------------------------------------------------------------------------------------------
        if TestHealthy:
            KidneyResult = self.case1
        elif TestTired:
            KidneyResult = self.case2
        elif TestDialysis:
            KidneyResult = self.case3
        else:
            KidneyResult = 'No Result'

        return KidneyResult

class SurigcalOperation:
    test1  = '(Hemoglopen)'
    test2  = '(White Blood)'
    test3  = '(Platelets)'
    test4  = '(Liver)'
    test5  = '(Kidney)'
    test6  = '(Fluidity)'
    #strings
    safe = '(None)'
    message = ', The patient has a problem with '
    splited =''
    patientResult = ''
    objectionResult = ''
    qualified = 'The patient is qualified, '
    unqualified = 'The patient is not qualified, '
    
    #checking patient's results
    def checkpatientResult(self, hemoglopen, whiteBlood, platelets, liver, kidney, fluidity):
        if 9 <= hemoglopen.data <= 11 and 5000.0 <= whiteBlood.data <= 18000.0 and 150000 <= platelets.data <= 350000 and \
        20 <= liver.data <= 40 and 0.5 <= kidney.data <= 1.5 and 0.7 <= fluidity.data <= 1.5:
            patientResult = self.qualified
        else:
            patientResult = self.unqualified
        return patientResult
    
    
