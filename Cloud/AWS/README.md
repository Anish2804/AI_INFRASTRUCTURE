# Virtualization & Virtual Machines (VMs)

## 1. Virtualization kya hai?

**Virtualization** ek technology hai jisme ek hi physical computer ke hardware resources:

* RAM
* CPU
* Storage

ka use karke **multiple Operating Systems** run kiye ja sakte hain.

---

## 2. Hypervisor ki Role

**Hypervisor** ek software hai jo virtualization ko possible banata hai.

Ye main/physical machine ke resources ko different parts mein divide karke **Virtual Machines (VMs)** create karta hai.

**Example:** Oracle VirtualBox

---

## 3. Virtual Machine (VM) kaise kaam karti hai?

Har VM ek **mini computer** ki tarah kaam karti hai.

VM **isolated** hoti hai.

Matlab:

> Ek VM mein hone wali problem normally main (host) machine ko affect nahi karti.

---

## 4. Types of Hypervisor

### Type 2 — Hosted Hypervisor

* Main Operating System (jaise Windows) ke upar install hota hai.
* Example: Oracle VirtualBox

```text
Hardware
   ↓
Host OS
   ↓
Type 2 Hypervisor
   ↓
VM
```

### Type 1 — Bare Metal Hypervisor

* Directly hardware par install hota hai.
* Iske liye alag Host OS ki zarurat nahi hoti.
* Servers mein use hota hai.
* Examples:

  * VMware vSphere
  * Citrix XenServer

```text
Hardware
   ↓
Type 1 Hypervisor
   ↓
VM
```

### Type 1 vs Type 2

| Type 1                    | Type 2                                     |
| ------------------------- | ------------------------------------------ |
| Directly hardware par     | Host OS ke upar                            |
| Host OS ki zarurat nahi   | Host OS required                           |
| Servers mein use hota hai | Desktop environments mein use ho sakta hai |

---

## 5. Virtualization ke Benefits

### 1. Cost & Space Saving

Multiple machines ko ek hi physical hardware par run kiya ja sakta hai.

### 2. Scalability

Requirement ke according resources ko **increase ya decrease** karna easy hota hai.

### 3. Maintenance

Cloud providers jaise **AWS** security aur updates ka responsibility lete hain, jisse company ka maintenance work easy ho jata hai.

---

# Quick Revision

* **Virtualization** → Ek physical computer par multiple OS run karna.
* **Hypervisor** → VMs create karta hai aur hardware resources manage/divide karta hai.
* **VM** → Ek isolated mini computer.
* **Type 2** → Host OS ke upar run hota hai.
* **Type 1** → Directly hardware par run hota hai.
* **Type 1** → Servers mein use hota hai.
* Virtualization ke benefits → **Cost/Space Saving + Scalability + Easier Maintenance**.






# Cloud Computing

## 1. Cloud Computing kya hai?

**Cloud Computing** ka matlab hai internet ke through IT resources ko **on-demand** use karna aur **Pay-as-you-go** basis par payment karna.

IT resources mein include ho sakte hain:

* Servers
* Storage
* Databases
* Software

### Examples

* Google Drive
* iCloud

### Major Cloud Providers

* AWS (Amazon Web Services)
* Microsoft Azure
* Google Cloud

---

## 2. Cloud kaise kaam karta hai?

Cloud providers ke paas large **Data Centers** hote hain.

Ye **Virtualization** ka use karke ek hi physical hardware ko multiple customers ke beech share karte hain.

```text
Large Data Center
       ↓
Physical Hardware
       ↓
Virtualization
       ↓
Multiple Customers
```

---

## 3. Cloud ki zarurat kyun hai?

Agar company apna business, jaise e-commerce, start karti hai toh khud:

* Servers purchase karne
* Security manage karne
* Backups manage karne

pad sakte hain.

Cloud provider ye infrastructure responsibilities handle karta hai, aur company resources ko rent/subscription basis par use kar sakti hai.

### Benefits

* **Scalability** → Resources ko requirement ke according increase/decrease karna easy.
* **Flexibility** → Infrastructure ko easily adjust kar sakte hain.

---

# 4. Cloud Computing Service Models

Cloud services ke 3 main models:

## IaaS — Infrastructure as a Service

Isme basic **infrastructure/hardware** rent par milta hai.

OS aur applications ko khud manage karna hota hai.

```text
IaaS
↓
Infrastructure
↓
You manage OS + Application
```

**Example analogy:** Khali shop — infrastructure available hai, baaki setup khud karna hai.

---

## PaaS — Platform as a Service

Isme **ready platform** milta hai.

Aap mainly apni **application** par focus karte ho; hardware aur OS ki concern nahi hoti.

```text
PaaS
↓
Ready Platform
↓
You focus on Application
```

**Example analogy:** Furniture aur machines wali ready shop.

---

## SaaS — Software as a Service

Isme **fully ready software** milta hai.

Kuch install/manage karne ki zarurat nahi; internet ke through directly access karte ho.

```text
SaaS
↓
Ready Software
↓
Just Use It
```

**Example analogy:** Ice-cream vending machine.

---

## IaaS vs PaaS vs SaaS

| IaaS                    | PaaS                  | SaaS             |
| ----------------------- | --------------------- | ---------------- |
| Infrastructure          | Ready Platform        | Ready Software   |
| OS khud manage          | OS ki concern nahi    | Kuch manage nahi |
| Application khud manage | Application par focus | Directly use     |

---

# 5. Cloud Deployment Models

## Public Cloud

* Shared environment
* Relatively cheaper aur easy
* Privacy comparatively kam

**Analogy:** Public Transport

---

## Private Cloud

* Sirf ek organization ke liye dedicated
* More control
* More security

**Analogy:** Rental Car

---

## Hybrid Cloud

**Public + Private Cloud** ka combination.

Sensitive data ko **Private Cloud** mein aur baaki resources ko **Public Cloud** mein rakha ja sakta hai.

```text
Hybrid Cloud
     │
 ┌───┴────┐
 ↓        ↓
Private  Public
Sensitive  Other
Data       Resources
```

---

# 6. Cloud mein sirf Servers nahi hote

Cloud providers multiple types ki services provide karte hain, jaise:

* Servers
* Databases
* Storage
* Machine Learning
* Monitoring
* Networking

---

# Quick Revision

* **Cloud Computing** → Internet ke through IT resources ko on-demand use karna + Pay-as-you-go.
* Cloud providers → **AWS, Azure, Google Cloud**
* Cloud providers large **Data Centers** use karte hain.
* **Virtualization** → Same hardware ko multiple customers ke beech share karne mein help karti hai.
* **IaaS** → Infrastructure milta hai.
* **PaaS** → Ready platform milta hai.
* **SaaS** → Ready software milta hai.
* **Public Cloud** → Shared environment.
* **Private Cloud** → Dedicated to one organization.
* **Hybrid Cloud** → Public + Private.
* Cloud services → Servers, Storage, Database, ML, Monitoring, Networking etc.
