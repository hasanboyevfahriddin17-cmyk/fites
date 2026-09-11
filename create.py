# -*- coding: utf-8 -*-
html_content = '''<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Smart Fitness & Body Diagnostics</title>

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet" />

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.3/dist/chart.umd.min.js"></script>

  <!-- Font Awesome CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />

  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            obsidian: { 900: '#07090E', 800: '#0B0F17', 700: '#111827', 600: '#1a2233' },
            emerald: { 400: '#34D399', 500: '#10B981', 600: '#059669' },
            cyan: { 400: '#22D3EE', 500: '#06B6D4' },
            amber: { 400: '#FBBF24', 500: '#F59E0B' },
            rose: { 400: '#FB7185', 500: '#F43F5E' },
          },
          fontFamily: { sans: ['"Plus Jakarta Sans"', 'sans-serif'] },
        }
      }
    };
  </script>

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background: #07090E;
      color: #E2E8F0;
      min-height: 100vh;
      overflow-x: hidden;
    }

    .bg-grid {
      position: fixed; inset: 0; z-index: 0; pointer-events: none;
      background-image:
        linear-gradient(rgba(16,185,129,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(16,185,129,0.03) 1px, transparent 1px);
      background-size: 40px 40px;
    }
    .bg-radial {
      position: fixed; inset: 0; z-index: 0; pointer-events: none;
      background: radial-gradient(ellipse 80% 60% at 50% -20%, rgba(16,185,129,0.08) 0%, transparent 70%),
                  radial-gradient(ellipse 60% 40% at 100% 100%, rgba(6,182,212,0.06) 0%, transparent 60%);
    }
    .floating-orb {
      position: fixed; border-radius: 50%; filter: blur(80px); pointer-events: none; z-index: 0;
      animation: float 8s ease-in-out infinite;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0px) scale(1); }
      50% { transform: translateY(-30px) scale(1.05); }
    }
    @keyframes slideIn {
      from { opacity: 0; transform: translateX(25px); }
      to { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeUp {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes shimmer {
      0% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
    }

    .glass {
      background: rgba(255, 255, 255, 0.03);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid rgba(255,255,255,0.07);
      border-radius: 1.25rem;
    }
    .glass-strong {
      background: rgba(255,255,255,0.05);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 1.25rem;
    }

    .step-dot {
      width: 36px; height: 36px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 0.75rem; font-weight: 700;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      position: relative; cursor: default;
    }
    .step-dot.active {
      background: linear-gradient(135deg, #10B981, #06B6D4);
      box-shadow: 0 0 0 4px rgba(16,185,129,0.25), 0 0 20px rgba(16,185,129,0.5);
      transform: scale(1.1);
    }
    .step-dot.completed {
      background: linear-gradient(135deg, #059669, #0891B2);
      box-shadow: 0 0 10px rgba(5,150,105,0.4);
    }
    .step-dot.pending {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      color: rgba(255,255,255,0.3);
    }

    .custom-slider {
      -webkit-appearance: none; appearance: none;
      width: 100%; height: 6px; outline: none;
      border-radius: 999px; cursor: pointer;
      background: rgba(255,255,255,0.1);
    }
    .custom-slider::-webkit-slider-thumb {
      -webkit-appearance: none; appearance: none;
      width: 22px; height: 22px; border-radius: 50%;
      background: linear-gradient(135deg, #10B981, #06B6D4);
      cursor: pointer;
      box-shadow: 0 0 0 3px rgba(16,185,129,0.3), 0 0 15px rgba(16,185,129,0.5);
      transition: all 0.2s;
    }
    .custom-slider::-webkit-slider-thumb:hover {
      transform: scale(1.15);
    }

    .card-option {
      border: 2px solid rgba(255,255,255,0.08);
      border-radius: 1rem; cursor: pointer;
      transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
      background: rgba(255,255,255,0.03);
      position: relative; overflow: hidden;
    }
    .card-option:hover {
      border-color: rgba(16,185,129,0.4);
      background: rgba(16,185,129,0.06);
      transform: translateY(-2px);
    }
    .card-option.selected {
      border-color: #10B981;
      background: rgba(16,185,129,0.12);
      box-shadow: 0 0 0 1px rgba(16,185,129,0.3), 0 8px 30px rgba(16,185,129,0.25);
    }
    .card-option .check-icon {
      display: none; position: absolute; top: 10px; right: 10px;
      width: 22px; height: 22px; border-radius: 50%;
      background: linear-gradient(135deg, #10B981, #06B6D4);
      align-items: center; justify-content: center; font-size: 0.65rem; color: white;
    }
    .card-option.selected .check-icon { display: flex; }

    .neo-input {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 0.75rem; color: #E2E8F0;
      font-weight: 600; outline: none;
      transition: all 0.2s;
    }
    .neo-input:focus {
      border-color: #10B981;
      box-shadow: 0 0 0 3px rgba(16,185,129,0.2);
    }

    .btn-primary {
      background: linear-gradient(135deg, #10B981, #06B6D4);
      border: none; border-radius: 0.875rem;
      font-weight: 700; cursor: pointer;
      box-shadow: 0 4px 20px rgba(16,185,129,0.35);
      transition: all 0.2s;
    }
    .btn-primary:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 25px rgba(16,185,129,0.5);
    }
    .btn-secondary {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 0.875rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s; color: rgba(255,255,255,0.7);
    }
    .btn-secondary:hover {
      background: rgba(255,255,255,0.1);
      color: white;
    }
    .btn-danger {
      background: rgba(244,63,94,0.1);
      border: 1px solid rgba(244,63,94,0.3);
      border-radius: 0.875rem; font-weight: 600;
      cursor: pointer; transition: all 0.2s; color: #FB7185;
    }
    .btn-danger:hover {
      background: rgba(244,63,94,0.2);
    }

    .gauge-container {
      position: relative; width: 200px; height: 105px; margin: 0 auto;
    }
    .gauge-bg {
      width: 200px; height: 100px;
      border-radius: 100px 100px 0 0;
      background: conic-gradient(from 180deg at 50% 100%, #3B82F6 0deg, #10B981 45deg, #FBBF24 90deg, #F97316 120deg, #EF4444 135deg, transparent 135deg);
      position: relative;
    }
    .gauge-needle {
      position: absolute; bottom: 0; left: 50%;
      width: 3px; height: 80px;
      background: linear-gradient(to top, #E2E8F0, rgba(255,255,255,0));
      transform-origin: bottom center;
      border-radius: 2px;
      transition: transform 1.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }
    .gauge-center {
      position: absolute; bottom: -6px; left: 50%;
      width: 16px; height: 16px; border-radius: 50%;
      background: linear-gradient(135deg, #10B981, #06B6D4);
      transform: translateX(-50%);
      box-shadow: 0 0 15px rgba(16,185,129,0.6);
    }

    .water-glass {
      width: 32px; height: 42px;
      border: 2px solid rgba(6,182,212,0.3);
      border-top: none; border-radius: 0 0 6px 6px;
      position: relative; overflow: hidden;
      transition: all 0.3s;
    }
    .water-glass.filled { border-color: #06B6D4; }
    .water-glass.filled .water-fill {
      background: linear-gradient(to top, #0891B2, #22D3EE);
      box-shadow: 0 0 10px rgba(6,182,212,0.5);
    }
    .water-fill {
      position: absolute; bottom: 0; left: 0; right: 0;
      height: 0%; transition: height 0.3s ease;
    }

    .progress-bar-inner {
      height: 100%; border-radius: 999px;
      background: linear-gradient(90deg, #10B981, #06B6D4, #10B981);
      background-size: 200% 100%;
      animation: shimmer 2s linear infinite;
    }

    .step-content { animation: slideIn 0.35s cubic-bezier(0.16, 1, 0.3, 1); }
    .dashboard-section { animation: fadeUp 0.4s ease-out forwards; }

    .alert-warning {
      background: rgba(245,158,11,0.08);
      border: 1px solid rgba(245,158,11,0.3);
      border-radius: 0.875rem;
    }
    .alert-danger {
      background: rgba(244,63,94,0.08);
      border: 1px solid rgba(244,63,94,0.3);
      border-radius: 0.875rem;
    }
    .alert-success {
      background: rgba(16,185,129,0.08);
      border: 1px solid rgba(16,185,129,0.3);
      border-radius: 0.875rem;
    }
    .alert-info {
      background: rgba(6,182,212,0.08);
      border: 1px solid rgba(6,182,212,0.3);
      border-radius: 0.875rem;
    }

    .badge {
      display: inline-flex; align-items: center; gap: 0.35rem;
      padding: 0.25rem 0.75rem; border-radius: 999px;
      font-size: 0.75rem; font-weight: 700;
    }

    .validation-msg { font-size: 0.8rem; font-weight: 500; margin-top: 0.5rem; }
    .validation-msg.error { color: #FB7185; }
    .validation-msg.success { color: #34D399; }
    .validation-msg.warning { color: #FBBF24; }

    .macro-pill {
      display: flex; align-items: center; gap: 0.75rem;
      padding: 0.75rem 1rem; border-radius: 0.75rem;
      font-size: 0.9rem; font-weight: 600;
    }

    @media print {
      body { background: #ffffff !important; color: #111827 !important; }
      .bg-grid, .bg-radial, .floating-orb, #stepper-section, .no-print { display: none !important; }
      #dashboard-section { display: block !important; padding: 0 !important; }
      .glass, .glass-strong { background: #f9fafb !important; border: 1px solid #e5e7eb !important; backdrop-filter: none !important; color: #111827 !important; }
      .text-white { color: #111827 !important; }
      .text-slate-400, .text-slate-500 { color: #4b5563 !important; }
      .alert-warning { background: #fffbeb !important; border-color: #fcd34d !important; color: #92400e !important; }
      .alert-danger { background: #fff1f2 !important; border-color: #fda4af !important; color: #9f1239 !important; }
      .alert-success { background: #f0fdf4 !important; border-color: #86efac !important; color: #166534 !important; }
      .alert-info { background: #ecfeff !important; border-color: #67e8f9 !important; color: #155e75 !important; }
      #print-header { display: block !important; }
    }
    #print-header { display: none; }
  </style>
</head>

<body>
  <div class="bg-grid"></div>
  <div class="bg-radial"></div>
  <div class="floating-orb" style="width:450px;height:450px;background:rgba(16,185,129,0.05);top:-100px;right:-100px;"></div>
  <div class="floating-orb" style="width:350px;height:350px;background:rgba(6,182,212,0.05);bottom:100px;left:-100px;animation-delay:-4s;"></div>

  <div class="relative z-10 min-h-screen flex flex-col">
    <!-- HEADER -->
    <header class="sticky top-0 z-50 py-4 px-6" style="background:rgba(7,9,14,0.85);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,0.05);">
      <div class="max-w-6xl mx-auto flex items-center justify-between">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-xl flex items-center justify-center" style="background:linear-gradient(135deg,rgba(16,185,129,0.2),rgba(6,182,212,0.2));border:1px solid rgba(16,185,129,0.3);">
            <i class="fa-solid fa-dna text-lg" style="color:#10B981;"></i>
          </div>
          <div>
            <h1 class="font-black text-lg leading-tight" style="background:linear-gradient(135deg,#10B981,#06B6D4);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Smart Fitness</h1>
            <p class="text-xs text-slate-500 font-medium">Body Diagnostics System</p>
          </div>
        </div>
        <div class="flex items-center gap-3">
          <div id="header-step-label" class="badge text-emerald-400" style="background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.2);">
            <i class="fa-solid fa-circle-dot text-xs"></i>
            <span>Boshlash</span>
          </div>
          <button id="print-btn" class="btn-secondary hidden px-4 py-2 text-sm items-center gap-2 no-print" onclick="window.print()">
            <i class="fa-solid fa-print text-xs"></i> Print / PDF
          </button>
          <button id="reset-btn" class="btn-danger hidden px-4 py-2 text-sm items-center gap-2 no-print" onclick="resetApp()">
            <i class="fa-solid fa-rotate-left text-xs"></i> Qayta hisoblash
          </button>
        </div>
      </div>
    </header>

    <!-- PRINT HEADER -->
    <div id="print-header" style="padding:20px 0 10px;border-bottom:2px solid #e5e7eb;margin-bottom:20px;">
      <h1 style="font-size:22pt;font-weight:900;color:#111827;">🧬 Smart Fitness & Body Diagnostics</h1>
      <p style="color:#6b7280;margin-top:4px;">Shaxsiy fitnes va biometric tahlil hisoboti</p>
      <p id="print-date" style="color:#9ca3af;font-size:10pt;margin-top:2px;"></p>
    </div>

    <!-- STEPPER SECTION -->
    <section id="stepper-section" class="flex-1 py-8 px-4 flex flex-col justify-center">
      <div class="max-w-3xl mx-auto w-full">

        <!-- Wizard Progress -->
        <div class="mb-8 glass-strong p-5">
          <div class="flex items-center justify-between mb-4 overflow-x-auto gap-1" id="step-indicators"></div>
          <div class="h-2 rounded-full" style="background:rgba(255,255,255,0.05);">
            <div id="progress-bar" class="progress-bar-inner rounded-full" style="width:11.11%;transition:width 0.4s ease;"></div>
          </div>
          <div class="flex justify-between mt-3 text-xs">
            <span id="step-counter" class="text-slate-500 font-medium">Qadam 1 / 9</span>
            <span id="step-name-label" class="font-bold" style="color:#10B981;">Jins tanlash</span>
          </div>
        </div>

        <!-- Step Body -->
        <div id="step-area"></div>

        <!-- Navigation Buttons -->
        <div class="flex items-center justify-between mt-6 gap-4">
          <button id="btn-prev" class="btn-secondary px-6 py-3.5 text-sm font-semibold flex items-center gap-2" onclick="prevStep()">
            <i class="fa-solid fa-arrow-left text-xs"></i> Ortga
          </button>
          <button id="btn-next" class="btn-primary px-8 py-3.5 text-sm text-white flex items-center gap-2" onclick="nextStep()">
            Davom etish <i class="fa-solid fa-arrow-right text-xs"></i>
          </button>
        </div>
      </div>
    </section>

    <!-- DASHBOARD SECTION -->
    <section id="dashboard-section" class="hidden py-8 px-4">
      <div class="max-w-6xl mx-auto" id="dashboard-content"></div>
    </section>
  </div>

  <script>
  const state = {
    step: 1,
    totalSteps: 9,
    answers: {
      gender: null,
      age: 25,
      height: 175,
      weight: 75,
      goal: null,
      activity: null,
      targetWeight: 70,
      durationWeeks: 10,
      waterIntake: 2.0,
      sleepHours: 7.5,
    },
    metrics: {},
    warnings: [],
    charts: {}
  };

  const STEP_NAMES = [
    'Jins tanlash',
    'Yosh va Bo\'y',
    'Hozirgi Vazn',
    'Asosiy Maqsad',
    'Faollik Darajasi',
    'Maqsadli Vazn',
    'Muddat (Haftalar)',
    'Kunlik Suv Iste\'moli',
    'Uyqu Davomiyligi',
  ];

  const ACTIVITY_OPTIONS = [
    { val: 1.2, label: 'Harakatsiz (Sedentary)', icon: 'fa-couch', desc: 'Kam harakatli ofis ishi, deyarli mashqsiz', color: '#94A3B8' },
    { val: 1.375, label: 'Engil faol (Light)', icon: 'fa-person-walking', desc: 'Haftasiga 1–3 kun engil mashg\'ulotlar', color: '#34D399' },
    { val: 1.55, label: 'O\'rtacha faol (Moderate)', icon: 'fa-dumbbell', desc: 'Haftasiga 3–5 kun o\'rtacha jismoniy mashqlar', color: '#10B981' },
    { val: 1.725, label: 'Juda faol (Heavy)', icon: 'fa-fire', desc: 'Haftasiga 6–7 kun muntazam og\'ir mashg\'ulot', color: '#F59E0B' },
    { val: 1.9, label: 'Professional sportchi', icon: 'fa-trophy', desc: 'Kuniga 2 mahal mashq yoki jismoniy og\'ir ish', color: '#EF4444' },
  ];

  const GOAL_OPTIONS = [
    { val: 'loss', label: 'Ozish (Yog\' Yoqish)', icon: 'fa-fire-flame-curved', desc: 'Tana yog\'ini kamaytirish, vazn tashlash', color: '#F59E0B', gradient: 'rgba(245,158,11,0.1)' },
    { val: 'maintain', label: 'Vaznni Saqlash', icon: 'fa-scale-balanced', desc: 'Mavjud holatni mustahkamlash, fitnes tonus', color: '#06B6D4', gradient: 'rgba(6,182,212,0.1)' },
    { val: 'gain', label: 'Massa / Mushak Qurish', icon: 'fa-person-arrow-up-from-line', desc: 'Sifatli mushak massasi va kuch to\'plash', color: '#10B981', gradient: 'rgba(16,185,129,0.1)' },
  ];

  function calculateDiagnostics() {
    const a = state.answers;

    // 1. BMR (Mifflin-St Jeor)
    let bmr = 0;
    if (a.gender === 'male') {
      bmr = 10 * a.weight + 6.25 * a.height - 5 * a.age + 5;
    } else {
      bmr = 10 * a.weight + 6.25 * a.height - 5 * a.age - 161;
    }

    // 2. TDEE
    const tdee = bmr * a.activity;

    // 3. BMI
    const hM = a.height / 100;
    const bmi = a.weight / (hM * hM);
    let bmiCategory = '', bmiColor = '';
    if (bmi < 18.5) { bmiCategory = 'Vazn yetishmasligi'; bmiColor = '#3B82F6'; }
    else if (bmi < 25) { bmiCategory = 'Normal vazn'; bmiColor = '#10B981'; }
    else if (bmi < 30) { bmiCategory = 'Ortiqcha vazn'; bmiColor = '#F59E0B'; }
    else { bmiCategory = 'Semizlik darajasi'; bmiColor = '#EF4444'; }

    const targetBMI = a.targetWeight / (hM * hM);

    // 4. Caloric Target
    let caloricTarget = 0;
    let deficitSurplus = 0;
    if (a.goal === 'loss') {
      caloricTarget = Math.round(tdee * 0.80); // 20% deficit
      deficitSurplus = caloricTarget - tdee;
    } else if (a.goal === 'maintain') {
      caloricTarget = Math.round(tdee);
      deficitSurplus = 0;
    } else {
      caloricTarget = Math.round(tdee * 1.12); // 12% surplus
      deficitSurplus = caloricTarget - tdee;
    }

    // 5. Macros
    let proteinG = 0, fatG = 0, carbG = 0;
    if (a.goal === 'loss') {
      proteinG = Math.round(a.weight * 2.1);
      fatG = Math.round(a.weight * 0.9);
    } else if (a.goal === 'gain') {
      proteinG = Math.round(a.weight * 2.0);
      fatG = Math.round(a.weight * 1.0);
    } else {
      proteinG = Math.round(a.weight * 1.7);
      fatG = Math.round(a.weight * 0.9);
    }
    const proteinKcal = proteinG * 4;
    const fatKcal = fatG * 9;
    const remainingKcal = Math.max(caloricTarget - proteinKcal - fatKcal, 0);
    carbG = Math.round(remainingKcal / 4);
    const carbKcal = carbG * 4;

    // 6. Water Calculation
    const waterReqML = a.weight * 38 + (a.activity - 1.2) * 600;
    const waterReqL = (waterReqML / 1000).toFixed(1);

    // 7. Trajectory
    const totalDiff = a.targetWeight - a.weight;
    const weeklyRate = totalDiff / a.durationWeeks;
    const trajectory = [];
    for (let w = 0; w <= a.durationWeeks; w++) {
      trajectory.push(+(a.weight + weeklyRate * w).toFixed(1));
    }

    // 8. Warnings & Penalties
    const warnings = [];
    if (a.sleepHours < 7) {
      warnings.push({
        type: 'danger',
        icon: 'fa-moon',
        title: 'Metabolik jarima: Uyqu yetishmovchiligi (-15%)',
        msg: `Kuniga atigi ${a.sleepHours} soat uxlashingiz kortizol darajasini oshiradi, tiklanish jarayonini va yog' yoqish tezligini ~15% ga pasaytiradi.`
      });
    }
    if (a.waterIntake < parseFloat(waterReqL) * 0.8) {
      warnings.push({
        type: 'warning',
        icon: 'fa-droplet',
        title: 'Energiya jarimasi: Gidratatsiya past (-10%)',
        msg: `Siz ${a.waterIntake}L suv ichyapsiz, tavsiya esa ${waterReqL}L. Tana suvsizlanganda mushak kuchi va metabolik tezlik taxminan 10% pasayadi.`
      });
    }
    if (Math.abs(weeklyRate) > 1.0 && a.goal === 'loss') {
      warnings.push({
        type: 'danger',
        icon: 'fa-triangle-exclamation',
        title: 'Xavfli tez vazn yo\'qotish!',
        msg: `Haftasiga o'rtacha ${Math.abs(weeklyRate).toFixed(2)} kg yo'qotish mushak erishiga va moddalar almashinuvining sekinlashishiga olib keladi. Optimal: haftasiga 0.5–1.0 kg.`
      });
    }

    // Scores
    const sleepScore = Math.min(Math.round((a.sleepHours / 8) * 100), 100);
    const hydraScore = Math.min(Math.round((a.waterIntake / parseFloat(waterReqL)) * 100), 100);
    const actScore = Math.round(((a.activity - 1.2) / 0.7) * 100);
    const calScore = 95;

    state.metrics = {
      bmr: Math.round(bmr),
      tdee: Math.round(tdee),
      bmi: +bmi.toFixed(1),
      bmiCategory,
      bmiColor,
      targetBMI: +targetBMI.toFixed(1),
      caloricTarget,
      deficitSurplus: Math.round(deficitSurplus),
      proteinG, fatG, carbG,
      proteinKcal, fatKcal, carbKcal,
      waterReqL,
      weeklyRate: +weeklyRate.toFixed(2),
      trajectory,
      sleepScore, hydraScore, actScore, calScore,
      totalScore: Math.round((sleepScore + hydraScore + actScore + calScore) / 4)
    };
    state.warnings = warnings;
  }

  function renderStepIndicators() {
    const container = document.getElementById('step-indicators');
    container.innerHTML = STEP_NAMES.map((name, i) => {
      const n = i + 1;
      let cls = n < state.step ? 'completed' : n === state.step ? 'active' : 'pending';
      const icon = n < state.step ? '<i class="fa-solid fa-check text-xs text-white"></i>' : `<span>${n}</span>`;
      return `
        <div class="flex flex-col items-center gap-1 min-w-[36px]">
          <div class="step-dot ${cls}">${icon}</div>
        </div>
      `;
    }).join('<div class="flex-1 h-px bg-white/10 mx-1"></div>');
  }

  function updateStepperProgress() {
    const pct = ((state.step - 1) / (state.totalSteps - 1)) * 100;
    document.getElementById('progress-bar').style.width = pct + '%';
    document.getElementById('step-counter').textContent = `Qadam ${state.step} / ${state.totalSteps}`;
    document.getElementById('step-name-label').textContent = STEP_NAMES[state.step - 1];
    document.getElementById('header-step-label').innerHTML = `<i class="fa-solid fa-circle-dot text-xs"></i><span>${STEP_NAMES[state.step-1]}</span>`;

    const prev = document.getElementById('btn-prev');
    const next = document.getElementById('btn-next');
    prev.style.visibility = state.step === 1 ? 'hidden' : 'visible';
    if (state.step === state.totalSteps) {
      next.innerHTML = '<i class="fa-solid fa-chart-line text-xs"></i> Diagnostikani Ko\'rish';
    } else {
      next.innerHTML = 'Davom etish <i class="fa-solid fa-arrow-right text-xs"></i>';
    }
    renderStepIndicators();
  }

  function renderCurrentStep() {
    const area = document.getElementById('step-area');
    area.innerHTML = '';
    const wrap = document.createElement('div');
    wrap.className = 'step-content glass-strong p-6 sm:p-8';
    wrap.innerHTML = getStepMarkup(state.step);
    area.appendChild(wrap);
    bindEventsForStep(state.step);
    updateStepperProgress();
  }

  function getStepMarkup(s) {
    switch(s) {
      case 1:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
              <i class="fa-solid fa-venus-mars"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Jinsingizni tanlang</h2>
              <p class="text-xs text-slate-400">Mifflin-St Jeor formulasi orqali asosiy metabolizm hisoblanadi</p>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-4">
            <div class="card-option p-6 text-center ${state.answers.gender === 'male' ? 'selected' : ''}" data-gender="male">
              <div class="check-icon"><i class="fa-solid fa-check"></i></div>
              <div class="text-5xl mb-3">👨</div>
              <div class="font-bold text-white text-lg">Erkak</div>
              <div class="text-xs text-slate-400 mt-1">BMR: +5 kcal qo'shiladi</div>
            </div>
            <div class="card-option p-6 text-center ${state.answers.gender === 'female' ? 'selected' : ''}" data-gender="female">
              <div class="check-icon"><i class="fa-solid fa-check"></i></div>
              <div class="text-5xl mb-3">👩</div>
              <div class="font-bold text-white text-lg">Ayol</div>
              <div class="text-xs text-slate-400 mt-1">BMR: -161 kcal tuzatish</div>
            </div>
          </div>
          <div id="v-msg" class="validation-msg"></div>
        `;
      case 2:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
              <i class="fa-solid fa-ruler-vertical"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Yosh va Bo'yingiz</h2>
              <p class="text-xs text-slate-400">Tana tuzilishi va biologik ko'rsatkichlar</p>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <div>
              <div class="flex justify-between items-center mb-2">
                <span class="text-sm font-semibold text-slate-300">Yosh (yil):</span>
                <span class="text-2xl font-black text-emerald-400" id="age-val">${state.answers.age}</span>
              </div>
              <input type="range" min="14" max="85" value="${state.answers.age}" class="custom-slider" id="age-slider" />
              <div class="flex justify-between text-xs text-slate-600 mt-1"><span>14 yosh</span><span>85 yosh</span></div>
            </div>
            <div>
              <div class="flex justify-between items-center mb-2">
                <span class="text-sm font-semibold text-slate-300">Bo'y (sm):</span>
                <span class="text-2xl font-black text-cyan-400" id="h-val">${state.answers.height}</span>
              </div>
              <input type="range" min="130" max="220" value="${state.answers.height}" class="custom-slider" id="h-slider" />
              <div class="flex justify-between text-xs text-slate-600 mt-1"><span>130 sm</span><span>220 sm</span></div>
            </div>
          </div>
        `;
      case 3:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400">
              <i class="fa-solid fa-weight-scale"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Hozirgi Vazningiz</h2>
              <p class="text-xs text-slate-400">Kalkulyatsiya asosi bo'lgan hozirgi tana vazni</p>
            </div>
          </div>
          <div class="text-center mb-6">
            <div class="text-6xl font-black text-amber-400 mb-1"><span id="w-val">${state.answers.weight}</span> <span class="text-2xl text-slate-400 font-normal">kg</span></div>
          </div>
          <input type="range" min="35" max="190" value="${state.answers.weight}" class="custom-slider" id="w-slider" />
          <div class="flex justify-between text-xs text-slate-600 mt-1 mb-5"><span>35 kg</span><span>190 kg</span></div>
          <div class="max-w-xs mx-auto">
            <label class="text-xs text-slate-400 block mb-1 text-center">Aniq son sifatida kiriting:</label>
            <input type="number" min="35" max="190" value="${state.answers.weight}" class="neo-input w-full p-2.5 text-center text-lg" id="w-input" />
          </div>
        `;
      case 4:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
              <i class="fa-solid fa-bullseye"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Asosiy Maqsadingiz</h2>
              <p class="text-xs text-slate-400">Kaloriya balansi va makronutrientlar shunga moslanadi</p>
            </div>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            ${GOAL_OPTIONS.map(g => `
              <div class="card-option p-5 ${state.answers.goal === g.val ? 'selected' : ''}" data-goal="${g.val}">
                <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                <div class="text-3xl mb-3" style="color:${g.color}"><i class="fa-solid ${g.icon}"></i></div>
                <div class="font-bold text-white text-base mb-1">${g.label}</div>
                <div class="text-xs text-slate-400 leading-relaxed">${g.desc}</div>
              </div>
            `).join('')}
          </div>
          <div id="v-msg" class="validation-msg"></div>
        `;
      case 5:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-rose-500/10 border border-rose-500/20 flex items-center justify-center text-rose-400">
              <i class="fa-solid fa-bolt"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Jismoniy Faollik Darajasi</h2>
              <p class="text-xs text-slate-400">TDEE (kunlik umumiy kaloriya sarfi) koeffitsienti</p>
            </div>
          </div>
          <div class="flex flex-col gap-3">
            ${ACTIVITY_OPTIONS.map(a => `
              <div class="card-option p-4 flex items-center gap-4 ${state.answers.activity === a.val ? 'selected' : ''}" data-activity="${a.val}">
                <div class="check-icon"><i class="fa-solid fa-check"></i></div>
                <div class="w-10 h-10 rounded-xl flex items-center justify-center shrink-0" style="background:${a.color}20;color:${a.color};border:1px solid ${a.color}40;">
                  <i class="fa-solid ${a.icon}"></i>
                </div>
                <div class="flex-1">
                  <div class="font-bold text-white text-sm">${a.label}</div>
                  <div class="text-xs text-slate-400">${a.desc}</div>
                </div>
                <div class="badge text-xs" style="background:${a.color}15;color:${a.color};border:1px solid ${a.color}30;">x${a.val}</div>
              </div>
            `).join('')}
          </div>
          <div id="v-msg" class="validation-msg"></div>
        `;
      case 6:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
              <i class="fa-solid fa-flag-checkered"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Maqsadli Tana Vazni</h2>
              <p class="text-xs text-slate-400">Erishmoqchi bo'lgan ideal vazningiz</p>
            </div>
          </div>
          <div class="text-center mb-6">
            <div class="text-6xl font-black text-purple-400 mb-1"><span id="tw-val">${state.answers.targetWeight}</span> <span class="text-2xl text-slate-400 font-normal">kg</span></div>
            <div class="text-xs text-slate-400" id="tw-diff-info">Farq: ${(state.answers.targetWeight - state.answers.weight).toFixed(1)} kg</div>
          </div>
          <input type="range" min="35" max="190" value="${state.answers.targetWeight}" class="custom-slider" id="tw-slider" />
          <div class="flex justify-between text-xs text-slate-600 mt-1 mb-4"><span>35 kg</span><span>190 kg</span></div>
          <div id="tw-alert" class="p-3 rounded-xl text-xs"></div>
        `;
      case 7:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-cyan-400">
              <i class="fa-solid fa-calendar-days"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Rejalashtirilgan Muddat</h2>
              <p class="text-xs text-slate-400">Maqsadga erishish uchun ajratilgan hafta soni</p>
            </div>
          </div>
          <div class="text-center mb-6">
            <div class="text-6xl font-black text-cyan-400 mb-1"><span id="dur-val">${state.answers.durationWeeks}</span> <span class="text-2xl text-slate-400 font-normal">hafta</span></div>
            <div class="text-xs text-slate-400">Taxminan ${Math.round(state.answers.durationWeeks / 4.3)} oy</div>
          </div>
          <input type="range" min="2" max="48" value="${state.answers.durationWeeks}" class="custom-slider" id="dur-slider" />
          <div class="flex justify-between text-xs text-slate-600 mt-1 mb-4"><span>2 hafta</span><span>48 hafta (1 yil)</span></div>
          <div id="dur-alert" class="p-3 rounded-xl text-xs"></div>
        `;
      case 8:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
              <i class="fa-solid fa-glass-water"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Kunlik Suv Iste'moli</h2>
              <p class="text-xs text-slate-400">Hozirda odatda qancha toza suv ichasiz?</p>
            </div>
          </div>
          <div class="text-center mb-4">
            <div class="text-6xl font-black text-cyan-400 mb-1"><span id="water-val">${state.answers.waterIntake}</span> <span class="text-2xl text-slate-400 font-normal">Litr</span></div>
            <div class="text-xs text-slate-400">(Taxminan ${Math.round(state.answers.waterIntake / 0.25)} stakan)</div>
          </div>
          <div class="flex justify-center gap-2 my-4 flex-wrap" id="water-glasses"></div>
          <input type="range" min="0.5" max="5.5" step="0.1" value="${state.answers.waterIntake}" class="custom-slider" id="water-slider" />
          <div class="flex justify-between text-xs text-slate-600 mt-1"><span>0.5 L</span><span>5.5 L</span></div>
        `;
      case 9:
        return `
          <div class="mb-6 flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
              <i class="fa-solid fa-moon"></i>
            </div>
            <div>
              <h2 class="text-xl font-bold text-white">Kunlik Uyqu Davomiyligi</h2>
              <p class="text-xs text-slate-400">Mushak tiklanishi, gormonal balans va yog' yonishi asosi</p>
            </div>
          </div>
          <div class="text-center mb-4">
            <div class="text-6xl font-black text-purple-400 mb-1"><span id="sleep-val">${state.answers.sleepHours}</span> <span class="text-2xl text-slate-400 font-normal">soat</span></div>
            <div class="text-xs" id="sleep-status"></div>
          </div>
          <input type="range" min="4" max="11" step="0.5" value="${state.answers.sleepHours}" class="custom-slider" id="sleep-slider" />
          <div class="flex justify-between text-xs text-slate-600 mt-1 mb-4"><span>4 soat</span><span>11 soat</span></div>
          <div class="grid grid-cols-3 gap-2 text-center text-xs">
            <div class="p-2.5 rounded-lg bg-rose-500/10 border border-rose-500/20 text-rose-300">&lt; 7 soat: Kortizol oshishi & samarasizlik</div>
            <div class="p-2.5 rounded-lg bg-emerald-500/10 border border-emerald-500/20 text-emerald-300">7–9 soat: Optimal biologik tiklanish</div>
            <div class="p-2.5 rounded-lg bg-cyan-500/10 border border-cyan-500/20 text-cyan-300">&gt; 9 soat: Haddan tashqari uzoq uyqu</div>
          </div>
        `;
    }
  }

  function bindEventsForStep(s) {
    if (s === 1) {
      document.querySelectorAll('[data-gender]').forEach(c => {
        c.addEventListener('click', () => {
          document.querySelectorAll('[data-gender]').forEach(x => x.classList.remove('selected'));
          c.classList.add('selected');
          state.answers.gender = c.dataset.gender;
          document.getElementById('v-msg').textContent = '';
        });
      });
    } else if (s === 2) {
      const ageS = document.getElementById('age-slider');
      const hS = document.getElementById('h-slider');
      ageS.addEventListener('input', () => {
        state.answers.age = +ageS.value;
        document.getElementById('age-val').textContent = state.answers.age;
      });
      hS.addEventListener('input', () => {
        state.answers.height = +hS.value;
        document.getElementById('h-val').textContent = state.answers.height;
      });
    } else if (s === 3) {
      const wS = document.getElementById('w-slider');
      const wI = document.getElementById('w-input');
      wS.addEventListener('input', () => {
        state.answers.weight = +wS.value;
        wI.value = state.answers.weight;
        document.getElementById('w-val').textContent = state.answers.weight;
      });
      wI.addEventListener('input', () => {
        const val = Math.min(Math.max(+wI.value || 35, 35), 190);
        state.answers.weight = val;
        wS.value = val;
        document.getElementById('w-val').textContent = val;
      });
    } else if (s === 4) {
      document.querySelectorAll('[data-goal]').forEach(c => {
        c.addEventListener('click', () => {
          document.querySelectorAll('[data-goal]').forEach(x => x.classList.remove('selected'));
          c.classList.add('selected');
          state.answers.goal = c.dataset.goal;
          document.getElementById('v-msg').textContent = '';
        });
      });
    } else if (s === 5) {
      document.querySelectorAll('[data-activity]').forEach(c => {
        c.addEventListener('click', () => {
          document.querySelectorAll('[data-activity]').forEach(x => x.classList.remove('selected'));
          c.classList.add('selected');
          state.answers.activity = +c.dataset.activity;
          document.getElementById('v-msg').textContent = '';
        });
      });
    } else if (s === 6) {
      const twS = document.getElementById('tw-slider');
      const updateTwNotice = () => {
        const diff = state.answers.targetWeight - state.answers.weight;
        document.getElementById('tw-val').textContent = state.answers.targetWeight;
        document.getElementById('tw-diff-info').textContent = `Farq: ${diff > 0 ? '+' : ''}${diff.toFixed(1)} kg`;
        const alertBox = document.getElementById('tw-alert');
        const hM = state.answers.height / 100;
        const targetBmi = state.answers.targetWeight / (hM * hM);
        if (targetBmi < 16 || targetBmi > 38) {
          alertBox.className = 'p-3 rounded-xl text-xs alert-danger';
          alertBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation mr-1.5"></i> Maqsadli BMI: ${targetBmi.toFixed(1)} (Juda xavfli ko'rsatkich!)`;
        } else {
          alertBox.className = 'p-3 rounded-xl text-xs alert-success';
          alertBox.innerHTML = `<i class="fa-solid fa-circle-check mr-1.5"></i> Maqsadli BMI: ${targetBmi.toFixed(1)} (Sog'lom va realistik diapazon)`;
        }
      };
      twS.addEventListener('input', () => {
        state.answers.targetWeight = +twS.value;
        updateTwNotice();
      });
      updateTwNotice();
    } else if (s === 7) {
      const durS = document.getElementById('dur-slider');
      const updateDurNotice = () => {
        const w = state.answers.durationWeeks;
        document.getElementById('dur-val').textContent = w;
        const diff = state.answers.targetWeight - state.answers.weight;
        const rate = Math.abs(diff / w);
        const alertBox = document.getElementById('dur-alert');
        if (rate > 1.0) {
          alertBox.className = 'p-3 rounded-xl text-xs alert-danger';
          alertBox.innerHTML = `<i class="fa-solid fa-triangle-exclamation mr-1.5"></i> Haftalik tezlik: ${rate.toFixed(2)} kg/hafta (Juda tez va xavfli! Muddatni uzaytiring)`;
        } else {
          alertBox.className = 'p-3 rounded-xl text-xs alert-success';
          alertBox.innerHTML = `<i class="fa-solid fa-circle-check mr-1.5"></i> Haftalik sur'at: ${rate.toFixed(2)} kg/hafta (Xavfsiz va barqaror marom)`;
        }
      };
      durS.addEventListener('input', () => {
        state.answers.durationWeeks = +durS.value;
        updateDurNotice();
      });
      updateDurNotice();
    } else if (s === 8) {
      const wS = document.getElementById('water-slider');
      const renderGlasses = (val) => {
        const glassesCount = Math.min(Math.round(val / 0.25), 16);
        const container = document.getElementById('water-glasses');
        container.innerHTML = Array.from({ length: 12 }, (_, i) => {
          const filled = i < glassesCount;
          return `
            <div class="water-glass ${filled ? 'filled' : ''}" data-gidx="${i + 1}">
              <div class="water-fill" style="height:${filled ? '100%' : '0%'}"></div>
            </div>
          `;
        }).join('');
      };
      wS.addEventListener('input', () => {
        state.answers.waterIntake = +parseFloat(wS.value).toFixed(1);
        document.getElementById('water-val').textContent = state.answers.waterIntake;
        renderGlasses(state.answers.waterIntake);
      });
      renderGlasses(state.answers.waterIntake);
    } else if (s === 9) {
      const slS = document.getElementById('sleep-slider');
      const updateSleepStatus = (val) => {
        const el = document.getElementById('sleep-status');
        if (val < 7) {
          el.className = 'text-xs text-rose-400 font-semibold';
          el.textContent = '⚠ Uyqu yetarli emas: -15% metabolizm sekinlashishi';
        } else if (val <= 9) {
          el.className = 'text-xs text-emerald-400 font-semibold';
          el.textContent = '✓ Ideal biologik me\'yor: Maksimal mushak va asab tiklanishi';
        } else {
          el.className = 'text-xs text-cyan-400 font-semibold';
          el.textContent = 'Uzoq uyqu davomiyligi';
        }
      };
      slS.addEventListener('input', () => {
        state.answers.sleepHours = +parseFloat(slS.value).toFixed(1);
        document.getElementById('sleep-val').textContent = state.answers.sleepHours;
        updateSleepStatus(state.answers.sleepHours);
      });
      updateSleepStatus(state.answers.sleepHours);
    }
  }

  function validateCurrentStep() {
    const s = state.step;
    const msgEl = document.getElementById('v-msg');
    if (s === 1 && !state.answers.gender) {
      if (msgEl) { msgEl.className = 'validation-msg error'; msgEl.textContent = 'Iltimos, jinsingizni tanlang!'; }
      return false;
    }
    if (s === 4 && !state.answers.goal) {
      if (msgEl) { msgEl.className = 'validation-msg error'; msgEl.textContent = 'Iltimos, maqsadingizni tanlang!'; }
      return false;
    }
    if (s === 5 && !state.answers.activity) {
      if (msgEl) { msgEl.className = 'validation-msg error'; msgEl.textContent = 'Iltimos, faollik darajangizni tanlang!'; }
      return false;
    }
    return true;
  }

  function nextStep() {
    if (!validateCurrentStep()) return;
    if (state.step < state.totalSteps) {
      state.step++;
      renderCurrentStep();
    } else {
      showDashboard();
    }
  }

  function prevStep() {
    if (state.step > 1) {
      state.step--;
      renderCurrentStep();
    }
  }

  function showDashboard() {
    calculateDiagnostics();
    document.getElementById('stepper-section').classList.add('hidden');
    const dashSec = document.getElementById('dashboard-section');
    dashSec.classList.remove('hidden');
    document.getElementById('print-btn').style.display = 'flex';
    document.getElementById('reset-btn').style.display = 'flex';
    document.getElementById('header-step-label').innerHTML = `<i class="fa-solid fa-chart-pie text-xs"></i><span>Diagnostika Natijasi</span>`;
    document.getElementById('print-date').textContent = `Hisobot vaqti: ${new Date().toLocaleDateString('uz-UZ', { year:'numeric', month:'long', day:'numeric' })}`;

    dashSec.querySelector('#dashboard-content').innerHTML = generateDashboardMarkup();
    setTimeout(() => {
      initCharts();
    }, 50);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function generateDashboardMarkup() {
    const m = state.metrics;
    const a = state.answers;
    const gObj = GOAL_OPTIONS.find(x => x.val === a.goal);
    const actObj = ACTIVITY_OPTIONS.find(x => x.val === a.activity);
    const bmiAngle = Math.min(Math.max(((m.bmi - 15) / 25) * 180 - 90, -90), 90);

    return `
      <!-- TOP STATUS -->
      <div class="glass-strong p-6 sm:p-8 mb-6 dashboard-section">
        <div class="flex flex-wrap items-center justify-between gap-4 mb-4">
          <div>
            <div class="badge text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 mb-2">
              <i class="fa-solid fa-check-double"></i> Tahlil Muvaffaqiyatli Yakunlandi
            </div>
            <h2 class="text-2xl sm:text-3xl font-black text-white">Biometrik Diagnostika Xulosasi</h2>
            <p class="text-xs sm:text-sm text-slate-400 mt-1">
              Maqsad: <strong class="text-white">${gObj.label}</strong> | Faollik: <strong class="text-slate-300">${actObj.label}</strong>
            </p>
          </div>
          <div class="flex items-center gap-3 no-print">
            <button onclick="window.print()" class="btn-primary px-5 py-2.5 text-sm text-white flex items-center gap-2">
              <i class="fa-solid fa-file-arrow-down"></i> Natijalarni Saqlash (PDF)
            </button>
            <button onclick="resetApp()" class="btn-danger px-4 py-2.5 text-sm flex items-center gap-2">
              <i class="fa-solid fa-rotate-left"></i> Qayta
            </button>
          </div>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-3 border-t border-white/10 text-xs">
          <div><span class="text-slate-500 block">Jins & Yosh:</span><strong class="text-white">${a.gender === 'male' ? 'Erkak' : 'Ayol'}, ${a.age} yosh</strong></div>
          <div><span class="text-slate-500 block">Bo'y & Vazn:</span><strong class="text-white">${a.height} sm, ${a.weight} kg</strong></div>
          <div><span class="text-slate-500 block">Maqsadli Vazn:</span><strong class="text-emerald-400">${a.targetWeight} kg (${a.durationWeeks} hafta)</strong></div>
          <div><span class="text-slate-500 block">Umumiy Ball:</span><strong class="text-cyan-400">${m.totalScore} / 100 ball</strong></div>
        </div>
      </div>

      <!-- WARNINGS -->
      ${state.warnings.length ? `
        <div class="mb-6 flex flex-col gap-3 dashboard-section">
          ${state.warnings.map(w => `
            <div class="alert-${w.type} p-4 flex gap-3 items-start">
              <div class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0 ${w.type === 'danger' ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30' : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'}">
                <i class="fa-solid ${w.icon}"></i>
              </div>
              <div>
                <div class="font-bold text-sm text-white mb-0.5">${w.title}</div>
                <div class="text-xs text-slate-300 leading-relaxed">${w.msg}</div>
              </div>
            </div>
          `).join('')}
        </div>
      ` : ''}

      <!-- KEY METRICS CARDS -->
      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-4 mb-6 dashboard-section">
        <div class="glass p-5">
          <div class="text-xs text-slate-400 font-semibold mb-1">BMI (Indeks)</div>
          <div class="text-3xl font-black" style="color:${m.bmiColor}">${m.bmi}</div>
          <div class="text-xs font-semibold mt-1" style="color:${m.bmiColor}">${m.bmiCategory}</div>
        </div>
        <div class="glass p-5">
          <div class="text-xs text-slate-400 font-semibold mb-1">BMR (Tinch holat)</div>
          <div class="text-3xl font-black text-emerald-400">${m.bmr}</div>
          <div class="text-xs text-slate-500 mt-1">kcal / kun</div>
        </div>
        <div class="glass p-5">
          <div class="text-xs text-slate-400 font-semibold mb-1">TDEE (Kunlik sarf)</div>
          <div class="text-3xl font-black text-cyan-400">${m.tdee}</div>
          <div class="text-xs text-slate-500 mt-1">kcal / kun</div>
        </div>
        <div class="glass p-5">
          <div class="text-xs text-slate-400 font-semibold mb-1">Maqsadli Kaloriya</div>
          <div class="text-3xl font-black text-amber-400">${m.caloricTarget}</div>
          <div class="text-xs font-medium mt-1 ${m.deficitSurplus < 0 ? 'text-rose-400' : 'text-emerald-400'}">
            ${m.deficitSurplus < 0 ? `${m.deficitSurplus} kcal defitsit` : m.deficitSurplus === 0 ? 'Balans' : `+${m.deficitSurplus} kcal surplyus`}
          </div>
        </div>
        <div class="glass p-5 col-span-2 sm:col-span-1">
          <div class="text-xs text-slate-400 font-semibold mb-1">Tavsiya Suv</div>
          <div class="text-3xl font-black text-blue-400">${m.waterReqL} <span class="text-base font-normal text-slate-400">L</span></div>
          <div class="text-xs text-slate-500 mt-1">Har kuni ichish shart</div>
        </div>
      </div>

      <!-- CHARTS SECTION 1: MACROS & BMI GAUGE -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6 dashboard-section">
        <!-- Macros -->
        <div class="glass-strong p-6">
          <h3 class="text-base font-bold text-white mb-4 flex items-center gap-2">
            <i class="fa-solid fa-chart-pie text-emerald-400"></i> Kunlik Makronutrientlar Tasimoti (BJU)
          </h3>
          <div class="grid grid-cols-3 gap-2 mb-4">
            <div class="macro-pill flex-col items-start bg-emerald-500/10 border border-emerald-500/20">
              <div class="text-xs text-slate-400">Oqsil (Protein)</div>
              <div class="text-xl font-black text-emerald-400">${m.proteinG}g</div>
              <div class="text-xs text-slate-500">${m.proteinKcal} kcal</div>
            </div>
            <div class="macro-pill flex-col items-start bg-amber-500/10 border border-amber-500/20">
              <div class="text-xs text-slate-400">Yog'lar (Fats)</div>
              <div class="text-xl font-black text-amber-400">${m.fatG}g</div>
              <div class="text-xs text-slate-500">${m.fatKcal} kcal</div>
            </div>
            <div class="macro-pill flex-col items-start bg-cyan-500/10 border border-cyan-500/20">
              <div class="text-xs text-slate-400">Uglevodlar (Carbs)</div>
              <div class="text-xl font-black text-cyan-400">${m.carbG}g</div>
              <div class="text-xs text-slate-500">${m.carbKcal} kcal</div>
            </div>
          </div>
          <div class="relative h-[220px]">
            <canvas id="chart-macros"></canvas>
          </div>
        </div>

        <!-- BMI Gauge -->
        <div class="glass-strong p-6 flex flex-col justify-between">
          <div>
            <h3 class="text-base font-bold text-white mb-2 flex items-center gap-2">
              <i class="fa-solid fa-gauge-high text-cyan-400"></i> Tana Massasi Indeksi (BMI) Shkalasi
            </h3>
            <p class="text-xs text-slate-400 mb-4\">Joriy holat va tana tuzilishi xavfsizlik darajasi</p>
          </div>
          <div class="py-4 text-center">
            <div class="gauge-container mb-4">
              <div class="gauge-bg"></div>
              <div class="gauge-needle" style="transform:rotate(${bmiAngle}deg);"></div>
              <div class="gauge-center"></div>
            </div>
            <div class="text-3xl font-black mb-1" style="color:${m.bmiColor}">${m.bmi}</div>
            <div class="text-sm font-semibold" style="color:${m.bmiColor}">${m.bmiCategory}</div>
            <div class="text-xs text-slate-500 mt-1">Maqsadli vazndagi BMI: <strong>${m.targetBMI}</strong></div>
          </div>
          <div class="grid grid-cols-4 gap-1 text-center text-xs pt-3 border-t border-white/10">
            <div class="text-blue-400">&lt;18.5<br><span class="text-slate-500">Kam vazn</span></div>
            <div class="text-emerald-400">18.5–24.9<br><span class="text-slate-500">Normal</span></div>
            <div class="text-amber-400">25–29.9<br><span class="text-slate-500">Ortiqcha</span></div>
            <div class="text-rose-400">&ge;30<br><span class="text-slate-500">Semizlik</span></div>
          </div>
        </div>
      </div>

      <!-- CHARTS SECTION 2: TRAJECTORY & RADAR -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6 dashboard-section">
        <!-- Weight Trajectory -->
        <div class="glass-strong p-6">
          <h3 class="text-base font-bold text-white mb-2 flex items-center gap-2">
            <i class="fa-solid fa-arrow-trend-down text-emerald-400"></i> Rejalashtirilgan Vazn Traektoriyasi
          </h3>
          <p class="text-xs text-slate-400 mb-4">Haftalik kutilayotgan o'zgarish: <strong>${m.weeklyRate > 0 ? '+' : ''}${m.weeklyRate} kg/hafta</strong></p>
          <div class="relative h-[240px]">
            <canvas id="chart-trajectory"></canvas>
          </div>
        </div>

        <!-- Radar Lifestyle -->
        <div class="glass-strong p-6">
          <h3 class="text-base font-bold text-white mb-2 flex items-center gap-2">
            <i class="fa-solid fa-heart-pulse text-purple-400"></i> Hayot Tarzi va Metabolizm Balansi
          </h3>
          <p class="text-xs text-slate-400 mb-4">Uyqu, suv, faollik va kaloriya mutanosibligi</p>
          <div class="relative h-[240px]">
            <canvas id="chart-radar"></canvas>
          </div>
        </div>
      </div>

      <!-- ACTION PLAN & TIMELINE -->
      <div class="glass-strong p-6 mb-6 dashboard-section">
        <h3 class="text-base font-bold text-white mb-4 flex items-center gap-2">
          <i class="fa-solid fa-list-check text-emerald-400"></i> Shaxsiy Tavsiyalar va Mashg'ulot Tartibi
        </h3>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs leading-relaxed">
          <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="font-bold text-sm text-emerald-400 mb-2 flex items-center gap-2"><i class="fa-solid fa-utensils"></i> Taomnoma Strategiyasi</div>
            <ul class="space-y-1.5 text-slate-300">
              <li>• Kuniga <strong>${m.caloricTarget} kcal</strong> dan oshirmaslik / kamaytirmaslik</li>
              <li>• Kunlik <strong>${m.proteinG}g oqsil</strong>ni 3-4 mahalga teng taqsimlash</li>
              <li>• Kechki 20:00 dan keyin og'ir uglevodlarni cheklash</li>
              <li>• Toza gazsiz suv miqdori kamida <strong>${m.waterReqL} litr</strong> bo'lishi</li>
            </ul>
          </div>
          <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="font-bold text-sm text-cyan-400 mb-2 flex items-center gap-2"><i class="fa-solid fa-dumbbell"></i> Jismoniy Yuklama</div>
            <ul class="space-y-1.5 text-slate-300">
              <li>• Haftasiga 3–4 kun 45–60 daqiqalik mashg'ulot</li>
              <li>• Kunlik qadamlar sonini 8,000–10,000 qadamga yetkazish</li>
              <li>• Mashqdan so'ng 10 daqiqa yengil cho'zilish (stretching)</li>
              <li>• Mushak o'sishi va yog' yoqish uchun progressiv yuklama</li>
            </ul>
          </div>
          <div class="p-4 rounded-xl bg-white/5 border border-white/10">
            <div class="font-bold text-sm text-purple-400 mb-2 flex items-center gap-2"><i class="fa-solid fa-bed"></i> Tiklanish va Rejim</div>
            <ul class="space-y-1.5 text-slate-300">
              <li>• Har kuni <strong>kamida 7.5–8 soat</strong> sifatli qorong'u xonada uxlash</li>
              <li>• Uyqudan 1 soat oldin telefon va ekranlardan foydalanmaslik</li>
              <li>• Har haftaning dushanba kuni tongda och qoringa vazn o'lchash</li>
              <li>• Natijalarni qayd qilib borish va har 4 haftada kaloriyani yangilash</li>
            </ul>
          </div>
        </div>
      </div>
    `;
  }

  function initCharts() {
    const m = state.metrics;
    const a = state.answers;

    // Macro Chart
    const ctxM = document.getElementById('chart-macros');
    if (ctxM) {
      if (state.charts.macro) state.charts.macro.destroy();
      state.charts.macro = new Chart(ctxM, {
        type: 'doughnut',
        data: {
          labels: ['Oqsil (g)', 'Yog\'lar (g)', 'Uglevodlar (g)'],
          datasets: [{
            data: [m.proteinG, m.fatG, m.carbG],
            backgroundColor: ['#10B981', '#F59E0B', '#06B6D4'],
            borderColor: '#07090E',
            borderWidth: 3,
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: { color: '#94A3B8', font: { size: 11, family: 'Plus Jakarta Sans' } }
            }
          },
          cutout: '70%'
        }
      });
    }

    // Trajectory Chart
    const ctxT = document.getElementById('chart-trajectory');
    if (ctxT) {
      if (state.charts.traj) state.charts.traj.destroy();
      const labels = state.metrics.trajectory.map((_, i) => i === 0 ? 'Boshlash' : `${i}-h`);
      state.charts.traj = new Chart(ctxT, {
        type: 'line',
        data: {
          labels,
          datasets: [{
            label: 'Prognoz Vazn (kg)',
            data: state.metrics.trajectory,
            borderColor: '#10B981',
            backgroundColor: 'rgba(16,185,129,0.1)',
            fill: true,
            tension: 0.35,
            pointBackgroundColor: '#10B981',
            pointRadius: 3
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false }
          },
          scales: {
            x: {
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { color: '#64748B', font: { size: 10 } }
            },
            y: {
              grid: { color: 'rgba(255,255,255,0.05)' },
              ticks: { color: '#64748B', font: { size: 10 } }
            }
          }
        }
      });
    }

    // Radar Chart
    const ctxR = document.getElementById('chart-radar');
    if (ctxR) {
      if (state.charts.radar) state.charts.radar.destroy();
      state.charts.radar = new Chart(ctxR, {
        type: 'radar',
        data: {
          labels: ['Uyqu sifati', 'Gidratatsiya', 'Faollik', 'Kaloriya intizomi'],
          datasets: [{
            label: 'Sizning ko\'rsatkichingiz',
            data: [m.sleepScore, m.hydraScore, m.actScore, m.calScore],
            backgroundColor: 'rgba(6,182,212,0.2)',
            borderColor: '#06B6D4',
            pointBackgroundColor: '#06B6D4',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            r: {
              suggestedMin: 0,
              suggestedMax: 100,
              angleLines: { color: 'rgba(255,255,255,0.08)' },
              grid: { color: 'rgba(255,255,255,0.08)' },
              pointLabels: { color: '#94A3B8', font: { size: 10 } },
              ticks: { display: false }
            }
          },
          plugins: {
            legend: { display: false }
          }
        }
      });
    }
  }

  function resetApp() {
    state.step = 1;
    state.answers.gender = null;
    state.answers.goal = null;
    state.answers.activity = null;
    document.getElementById('dashboard-section').classList.add('hidden');
    document.getElementById('stepper-section').classList.remove('hidden');
    document.getElementById('print-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'none';
    renderCurrentStep();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    if (!document.getElementById('stepper-section').classList.contains('hidden')) {
      if (e.key === 'Enter') nextStep();
    }
  });

  // START
  renderCurrentStep();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
print("SUCCESS")
